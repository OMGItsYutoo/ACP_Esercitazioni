import grpc
import argparse
from grpc_package.proto import statistics_pb2, statistics_pb2_grpc

def run(port):
    
    channel=grpc.insecure_channel(f"localhost:{str(port)}")
    stub=statistics_pb2_grpc.StatisticsStub(channel)
    
    print('[Dashbooard] - Sending request for availabe sensors')

    results=stub.getSensors(statistics_pb2.Empty())
    sensors=[]
    
    for res in results:
        print(f"[Dashboard] - Received sensor_id: {res.sensor_id}, data_type: {res.data_type}")
        sensors.append(res)
        
    for sensor in sensors:
        print(f"[Dashboard] - Sending mean request for sensor_id: {sensor.sensor_id}, data_type: {sensor.data_type}")
        response=stub.getMean(statistics_pb2.MeanRequest(sensor_id=sensor.sensor_id,data_type=sensor.data_type))
        print(f'[Dashboard] - Mean: {response.mean}')
        
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("port", help="port on which the statistics server is listening")
    args=parser.parse_args()
    
    run(args.port)
        