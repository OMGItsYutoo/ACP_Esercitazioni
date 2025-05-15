import ordermanagement_pb2_grpc
import ordermanagement_pb2


import grpc
import time
import sys
import multiprocess as mp

def run(port):
    channel=grpc.insecure_channel("localhost:"+str(port))
    
    stub=ordermanagement_pb2_grpc.OrderManagementStub(channel)
    
    orders=[]
    orders.append(ordermanagement_pb2.Order(items=['A','B','A','B'], price=2000.00, description='La madonna è una brava donna',destination="RRRRRROOOOOMAAAAA"))
    orders.append(ordermanagement_pb2.Order(items=['A','B','ACCIPICCHIA','B'], price=1000.00, description='La malonna è una brava donna',destination="NAAAAAAAAPL"))
    
    
    for order in orders:
        response=stub.addOrder(order)
        print("addOrder invocation...... response:", response)
        order = stub.getOrder(response)
        print("getOrder() invoked. Response: ", order)
        
    item_to_find=ordermanagement_pb2.StringMessage(id='A')
    orders_found=stub.searchOrders(item_to_find)
    for order in orders_found:
        print("SearchOrders gave: ", order)
        
        
    orders_to_be_processed=generate_orders_for_processing()
    shipms_list=stub.processOrders(orders_to_be_processed)
    
    for shipm in shipms_list:
        print(shipm)

def generate_orders_for_processing():

    print("Generating orders to delivery...")

    ord1 = ordermanagement_pb2.Order(
        id='104', price=2332,
        items=['Item - A', 'Item - B'],  
        description='Updated desc', 
        destination='San Jose, CA')
    
    ord2 = ordermanagement_pb2.Order(
        id='105', price=3000, 
        description='Updated desc', 
        destination='San Francisco, CA')
    
    ord3 = ordermanagement_pb2.Order(
        id='106', price=2560, 
        description='Updated desc', 
        destination='San Francisco, CA')
    
    ord4 = ordermanagement_pb2.Order(
        id='107', price=2560, 
        description='Updated desc', 
        destination='Mountain View, CA')
    
    list = [ord1,ord2,ord3,ord4]

    for processing_orders in list:
        yield processing_orders

if __name__=="__main__":
    try:
        port=sys.argv[1]
    except:
        print("Ma si strunz, c manc o port")
        
    run(port)