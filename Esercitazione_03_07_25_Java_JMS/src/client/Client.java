package client;

import java.util.Hashtable;
import java.util.Random;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class Client {
    private static final int N = 10;
    
    public static void main(String[] args) {
        
        Hashtable<String, String> prop=new Hashtable<String, String>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
		prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("queue.risposta", "risposta");
        prop.put("queue.richiesta", "richiesta");

        try {
            Context ctx=new InitialContext(prop);

            QueueConnectionFactory qconnf=(QueueConnectionFactory) ctx.lookup("QueueConnectionFactory");
            Queue queueRequest=(Queue) ctx.lookup("richiesta");
            Queue queueResponse=(Queue) ctx.lookup("risposta");

            QueueConnection qconn=qconnf.createQueueConnection();
            qconn.start();

            QueueSession qSession=qconn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueReceiver qReceiver=qSession.createReceiver(queueResponse);
            qReceiver.setMessageListener(new ClientListener());

            QueueSender qSender=qSession.createSender(queueRequest);

            MapMessage mm=qSession.createMapMessage();

            for (int i=0;i<N;i++){
                if(i%2==0){
                    mm.setString("operation", "preleva");
                    
                    mm.setJMSReplyTo(queueResponse);
                    
                    qSender.send(mm);
                    System.out.println("[Client] - Sent a preleva message");
                }else{
                    mm.setString("operation", "deposita");
                    Random r = new Random();
				    int randomValue = r.nextInt(100);
                    mm.setInt("value", randomValue);
                                        
                    qSender.send(mm);
                    
                    System.out.println("[Client] - Sent a deposita message");
                }
            }

            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            qconn.close();

        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        }

    }
}
