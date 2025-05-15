from concurrent import futures
import uuid
import logging
import grpc
import ordermanagement_pb2_grpc
import ordermanagement_pb2

class OrderManagementImpl(ordermanagement_pb2_grpc.OrderManagementServicer):
    
    def __init__(self):
        self.orderDict={}
    
    def addOrder(self, request:ordermanagement_pb2.Order, context):
        id=uuid.uuid1()
        request.id=str(id)  
        self.orderDict[request.id]=request
        response = ordermanagement_pb2.StringMessage(id=str(id))
        
        logging.debug('[OrderManagementServicer] addOrder: addedd order with ID: ' + str(id))
        return response
    
    def getOrder(self, request, context):
        order = self.orderDict.get(request.id)
        if order is not None: 
            logging.debug('[OrderManagementServicer] getOrder: returning order ' + str(order))
            return order
        else: 
            # Error handling 
            logging.debug('[OrderManagementServicer] getOrder: Order not found ' + request.value)

            # Usare set_code() per impostare il valore da usare come status code quando la RPC completa con errore
            # per gli StatusCode vedere: https://grpc.github.io/grpc/python/_modules/grpc.html#StatusCode

            context.set_code(grpc.StatusCode.NOT_FOUND)

            # Usare set_details() per impostare il valore da usare come stringa di dettaglio quando la RPC completa
            # con errore.

            context.set_details('Order : ', request.value, ' Not Found.')

            # ritorno un Order vuoto in caso di errore
            return ordermanagement_pb2.Order()
         
    # Server Streaming 
    def searchOrders(self, request:ordermanagement_pb2.Order, context):  
        logging.debug('[OrderManagementServicer] searchOrders: searching for orders with item equal to: ' + request.id)
        matching_orders = self.searchInventory(request.id)
        for order in matching_orders:
            yield order #generator function
            
    # Local function 
    def searchInventory(self, query):
        matchingOrders = []    
        for order_id, order in self.orderDict.items(): 
            if query in order.items:
                    matchingOrders.append(order)
                    
        return matchingOrders
    
    def processOrders(self, request_iterator, context):
        
        logging.debug('[OrderManagementServicer] processOrders: processing orders for shipping...')

        location_dict = {}

        for order in request_iterator:

            if order.destination not in location_dict.keys():
                location_dict[order.destination] = [order]
                #print(location_dict[order.destination])
                
            else:
                """
                {'Napoli': [
                    id: "3632b44c-0c94-11ef-bf4b-acde48001122"
                items: "Item - A"
                items: "Item - B"
                items: "Item - C"
                description: "This is a Sample order - 1 : description."
                price: 2450.5
                destination: "San Jose, CA"
                
                id: "3632b44c-0c94-11ef-bf4b-acde48001122"
                items: "Item - A"
                items: "Item - B"
                items: "Item - C"
                description: "This is a Sample order - 1 : description."
                price: 2450.5
                destination: "San Jose, CA"]
                }
                """
                #lista_ordini = location_dict[order.destination]
                #lista_ordini.append(order)
                location_dict[order.destination].append(order)
                #print(location_dict[order.destination])
                
            
        
        for key, values in location_dict.items():

            shipment_id = uuid.uuid1()
            shipment = ordermanagement_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', orders=values)
            # shipment = order_management_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', orders=values) ### EQUIVALENTE
            
            yield shipment
            logging.debug('[OrderManagementServicer] processOrders: processed shipment: ' + str(shipment_id))

        logging.debug('[OrderManagementServicer] processOrders: processing orders completed!')
        

def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=(('grpc.so_reuseport',0),)) #non si possono utilizzare i processi
    
    ordermanagement_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementImpl(),server)
    
    port=1212
    server.add_insecure_port("[::]:"+str(port))
    server.start()
    print("server in ascolto sul porto 1212")
    
    server.wait_for_termination()
    
if __name__=="__main__":
    serve()
    
    