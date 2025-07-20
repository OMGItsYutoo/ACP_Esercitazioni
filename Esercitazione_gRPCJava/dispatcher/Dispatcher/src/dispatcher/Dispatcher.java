package dispatcher;

import java.util.Hashtable;
import java.util.concurrent.TimeUnit;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

import io.grpc.Grpc;
import io.grpc.InsecureChannelCredentials;
import io.grpc.ManagedChannel;

public class Dispatcher {
    
    public static void main(String[] args) {

        if(args.length!=1){
            System.out.println("Please specify the port the server is listening on.");
            System.exit(1);
        }

        Hashtable<String, String> prop=new Hashtable<>();
        
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("queue.request", "request");

        ManagedChannel channel=null;
        try {
            Context cnx=new InitialContext(prop);
            
            QueueConnectionFactory qConnectionFactory=(QueueConnectionFactory) cnx.lookup("QueueConnectionFactory");
            Queue qRequest=(Queue) cnx.lookup("request");

            QueueConnection qConnection=qConnectionFactory.createQueueConnection();
            qConnection.start();

            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver qReceiver=qSession.createReceiver(qRequest);

            //java gRPC
            int port=Integer.valueOf(args[0]);
            String target="localhost:"+port;

            channel=Grpc.newChannelBuilder(target, InsecureChannelCredentials.create()).build();   
            MagazzinoGrpc.MagazzinoBlockingStub stub=MagazzinoGrpc.newBlockingStub(channel);         

            qReceiver.setMessageListener(new DispatcherListener(qConnection, stub));

            System.out.println("[Dispatcher_Java] - Dispatcher avviato");

            while (true) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    break;
                }
            }

            qReceiver.close();
            qSession.close();
            qConnection.close();
        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        } finally{
            try{
                channel.shutdownNow().awaitTermination(60, TimeUnit.SECONDS);
            }catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}
