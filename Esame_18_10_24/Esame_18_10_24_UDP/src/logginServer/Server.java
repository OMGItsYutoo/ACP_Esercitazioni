package logginServer;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class Server {

    private static final int PORT=12122;
    
    public static void main(String[] args) {
        
        Hashtable <String, String> prop=new Hashtable<>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("queue.error", "error");
        prop.put("queue.info", "info");
    
        
        try {
            Context cnx=new InitialContext(prop);
            
            QueueConnectionFactory qConnectionFactory=(QueueConnectionFactory) cnx.lookup("QueueConnectionFactory");
            Queue errorQueue=(Queue) cnx.lookup("error");
            Queue infoQueue=(Queue) cnx.lookup("info");

            QueueConnection qConnection=qConnectionFactory.createQueueConnection();
            qConnection.start();

            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            LogginImpl serverImpl=new LogginImpl(PORT, qConnection, errorQueue, infoQueue);
            serverImpl.runSkeleton();
            

            qSession.close();
            qConnection.close();
        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
    
}
