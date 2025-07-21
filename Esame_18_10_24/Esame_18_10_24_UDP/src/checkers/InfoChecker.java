package checkers;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class InfoChecker {
    public static void main(String[] args) {

        Hashtable <String, String> prop=new Hashtable<>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("queue.info", "info");

        try {
            Context cnx=new InitialContext(prop);

            QueueConnectionFactory qConnectionFactory=(QueueConnectionFactory) cnx.lookup("QueueConnectionFactory");
            Queue infoQueue=(Queue) cnx.lookup("info");

            QueueConnection qConnection=qConnectionFactory.createQueueConnection();
            qConnection.start();

            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver qReceiver=qSession.createReceiver(infoQueue);
            qReceiver.setMessageListener(new InfoListener());

        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
