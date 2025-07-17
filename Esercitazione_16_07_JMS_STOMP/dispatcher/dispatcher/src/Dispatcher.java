import java.util.Hashtable;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class Dispatcher {
    public static void main(String[] args) {
        
        if(args.length!=1){
            System.out.println("Please insert the port the server is listening on.");
            System.exit(1);
        }

        int port=Integer.valueOf(args[0]);

        Hashtable<String, String> prop= new Hashtable<String, String>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");


        prop.put("queue.requests", "requests");
        prop.put("queue.responses", "responses");

        try {
            Context ctx=new InitialContext(prop);

            QueueConnectionFactory qconnf=(QueueConnectionFactory) ctx.lookup("QueueConnectionFactory");
            Queue requestsQueue=(Queue) ctx.lookup("requests");

            QueueConnection qConnection=qconnf.createQueueConnection();
            qConnection.start();

            System.out.println("[Dispatcher_Java] - Dispatcher started");

            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver qReceiver=qSession.createReceiver(requestsQueue);
            qReceiver.setMessageListener(new DispatcherListener(qConnection, "localhost", port));

        } catch (NamingException e) {
            System.out.println("[Dispatcher_Java] - Exception: "+e.getMessage());
        } catch (JMSException e) {
            System.out.println("[Dispatcher_Java] - Exception: "+e.getMessage());
        }

    }
}
