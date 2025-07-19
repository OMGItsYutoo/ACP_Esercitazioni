import java.util.Hashtable;
import java.util.Random;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Session;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.jms.Topic;
import javax.naming.NamingException;

public class Client {

    final static int n_req=20;
    final static String[] req_type = {"buy", "stats"};
    final static String[] artists={"Jovanotti", "Ligabue", "Negramaro"};

    public static void main(String[] args){

        if(args.length!=1){
            System.out.println("Esempio di utilizzo: java nomepackage.Client tipoRichiesta");
            System.exit(1);
        }

        String request=args[0];

        if(!request.equalsIgnoreCase("buy") && !request.equalsIgnoreCase("stats")){
            System.out.println("La richiesta può essere esclusivamente di tipo buy o stats");
            System.exit(1);
        }

        Hashtable<String, String> prop=new Hashtable<String, String>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("topic.request", "request");

        try {
            Context cnx=new InitialContext(prop);
            
            TopicConnectionFactory tConnectionFactory=(TopicConnectionFactory) cnx.lookup("TopicConnectionFactory");
            Topic requestTopic=(Topic) cnx.lookup("request");

            TopicConnection tConnection=tConnectionFactory.createTopicConnection();
            tConnection.start();

            TopicSession tSession=tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicPublisher tPublisher=tSession.createPublisher(requestTopic);


            Random rand=new Random();

            for(int i=0; i<n_req;i++){
                MapMessage mm=tSession.createMapMessage();

                mm.setString("type", request);

                if(request.equalsIgnoreCase("buy")){
                    mm.setString("value", artists[rand.nextInt(Client.artists.length)]);
                }else{
                    mm.setString("value", "Sold");
                }

                tPublisher.publish(mm);

                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            
            tPublisher.close();
            tSession.close();
            tConnection.close();
        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
