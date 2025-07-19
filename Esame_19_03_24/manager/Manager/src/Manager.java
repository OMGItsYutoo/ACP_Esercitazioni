import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.Session;
import javax.jms.Topic;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicSession;
import javax.jms.TopicSubscriber;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class Manager {
    public static void main(String[] args){
        
        Hashtable<String, String> prop=new Hashtable<String, String>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("topic.request", "request");
        prop.put("topic.tickets", "tickets");
        prop.put("topic.stats", "stats");

        Context cnx;
        try {
            cnx = new InitialContext(prop);

            TopicConnectionFactory tConnectionFactory=(TopicConnectionFactory) cnx.lookup("TopicConnectionFactory");
            Topic topicRequest=(Topic) cnx.lookup("request");
            Topic topicStats=(Topic) cnx.lookup("stats");
            Topic topicTickets=(Topic) cnx.lookup("tickets");

            TopicConnection tConnection=tConnectionFactory.createTopicConnection();
            tConnection.start();

            TopicSession tSession=tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicSubscriber tSubscriber=tSession.createSubscriber(topicRequest);

            tSubscriber.setMessageListener(new ManagerListener(tSession,topicStats,topicTickets));

            System.out.println("[Manager] - Manager avviato");

            while (true) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    break;
                }
            }
            
            tSubscriber.close();
            tSession.close();
            tConnection.close();
        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        }



    }
}
