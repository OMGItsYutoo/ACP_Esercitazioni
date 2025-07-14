from proto import statistics_pb2, statistics_pb2_grpc
    
class StatisticsImpl(statistics_pb2_grpc.StatisticsServicer):
    def __init__(self, db):
        self.db=db
    
    def getSensors(self, request, context):
        sens_collection=self.db["sensors"]
        
        print("[StatisticsImpl] - Getting sensors from db")
        
        sensors=sens_collection.find()
        
        for s in sensors:
            
            print(f"[StatisticsImpl] - Got sensor: {s}")
            
            sensor_id=s["_id"]
            data_type=s["data_type"]
            
            yield statistics_pb2.Sensor(sensor_id=sensor_id, data_type=data_type)
            
    def getMean(self, request, context):
        sensor_id=request.sensor_id
        data_type=request.data_type
        
        if data_type not in ["temp","press"]:
            return statistics_pb2.StringMessage(response="Couldn't recongnize data_type")
    
        collection=self.db[data_type+"_data"]
        
        data=collection.find({"sensor_id":sensor_id})    
        
        s=0
        count=0
        for d in data:
            value=d["data"]
            s+=value
            count+=1
            
        mean=s/count
        
        print(f"[StatisticsImpl] - Mean is: {mean}")
        return statistics_pb2.StringMessage(response=str(mean))
            
                    