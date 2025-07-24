from proto import statistics_pb2_grpc, statistics_pb2

class StatisticsImpl(statistics_pb2_grpc.StatisticsServicer):
    def __init__(self, db):
        self.db=db
    
    def getSensors(self, request, context):
        
        sensor_collection=self.db["sensors"]
        
        print("[StatisticsImpl] - Getting sensors from the databse")
        
        sensor_curs=sensor_collection.find()
        
        for sens in sensor_curs:
            
            print(f"[StatisticsImpl] - Got {sens} from the db")
            
            sensor_id=sens["_id"]
            data_type=sens["data_type"]
            
            yield statistics_pb2.Sensor(sensor_id=sensor_id, data_type=data_type)
            
    def getMean(self, request, context):
        sensor_id=request.sensor_id
        data_type=request.data_type
        
        if data_type not in ["temp", "press"]:
            print(f"[StatisticsImpl] - Could not recognized the data type: {data_type}")
            return statistics_pb2.StringMessage(mean="Failure")
        
        collection=self.db[data_type+"_data"]
        data=collection.find({"sensor_id":sensor_id})
        
        s=0
        cnt=0
        for mis in data:
            value=mis["data"]
            s+=value
            cnt+=1
            
        avg=s/cnt
        
        print(f"[StatisticsImpl] - Mean is {avg}")
        
        return statistics_pb2.StringMessage(mean=str(avg))