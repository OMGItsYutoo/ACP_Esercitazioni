package checkers;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class ErrorCkecker {
    
    public static void main(String[] args) {
        if(args.length!=1){
            System.out.println("[InfoChecker] - Please insert type of error checker.");
            System.exit(1);
        }

        String type=new String(args[0]);

        Hashtable <String, String> prop=new Hashtable<>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("queue.error", "error");

        try {
            Context cnx=new InitialContext(prop);

            QueueConnectionFactory qConnectionFactory=(QueueConnectionFactory) cnx.lookup("QueueConnectionFactory");
            Queue errorQueue=(Queue) cnx.lookup("error");

            QueueConnection qConnection=qConnectionFactory.createQueueConnection();
            qConnection.start();

            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver qReceiver=qSession.createReceiver(errorQueue);
            qReceiver.setMessageListener(new ErrorListener(type));

        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        }        
    }
}
