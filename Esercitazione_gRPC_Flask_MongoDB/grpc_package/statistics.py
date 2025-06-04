import grpc
from proto import statistics_pb2, statistics_pb2_grpc
from pymongo import MongoClient
from concurrent import futures
import time
import grpc

def get_database():
    client=MongoClient("localhost",27017)
    return client["sensors_data"]

class StatisticsServicer(statistics_pb2_grpc.StatisticsServicer):
    def __init__(self, db):
        self.db=db
    
    def getSensors(self, request, context):
        sensor_coll=self.db["sensors"]
        
        print("[StatisticsServicer] - Getting the sensors from db")
      
        cursor=sensor_coll.find()
        for c in cursor:
            print(f"[StatisticsServicer] - Got {str(c)}")
            
            try:
                
                sensor_id=c["_id"]
                data_type=c["data_type"]
            except KeyError:
                print("[StatisticsServicer] - Failed retrieving one of the required field...skipping the data")
                print("[StatisticsServicer] - Obtaianed - " + str(c))
                continue
            
            yield statistics_pb2.Sensor(sensor_id=sensor_id,data_type=data_type)
            
    def getMean(self, request, context):
        
        sensor_id=request.sensor_id
        data_type=request.data_type
        
        print(f"[StatisticsServicer] - Received mean request for sensord_id: {sensor_id} - data_type: {data_type}")

        if data_type not in  ["temp","press"]:
            return statistics_pb2.MeanResponse(mean=-1)
        else:
            collection=self.db[data_type+"_data"]
        
        cursor=collection.find({"sensor_id":sensor_id})
        
        sum=0
        count=0
        for c in cursor:
            try:
                data=c["data"]
                sum+=data
                count+=1
            except KeyError:
                print("[StatisticsServicer] - Failed retrieving one of the required field...skipping the data")
                
        mean=sum/count
        
        print(f"[StatisticsServicer] - The mean is: {str(mean)}")
        
        return statistics_pb2.MeanResponse(mean=mean)
    
def main():
    db=get_database()
    
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    statistics_pb2_grpc.add_StatisticsServicer_to_server(StatisticsServicer(db),server)
    
    port=server.add_insecure_port("localhost:0")
    print('Starting server. Listening on port ' + str(port))
    
    server.start()
    
    time.sleep(60)
    
    server.wait_for_termination()

if __name__=="__main__":
    main()
