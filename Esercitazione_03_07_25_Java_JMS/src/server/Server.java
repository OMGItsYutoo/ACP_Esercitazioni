package server;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

import coda.Coda;
import coda.CodaCircolare;
import coda.CodaWrapperSynch;

public class Server {
    public static void main(String[] args) {
        Hashtable<String, String> p=new Hashtable<String, String>();

        p.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        p.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        p.put("queue.richiesta", "richiesta");

        try{
            Context cnt=new InitialContext(p);

            QueueConnectionFactory qconnf=(QueueConnectionFactory)cnt.lookup("QueueConnectionFactory");
            Queue queueRequest=(Queue)cnt.lookup("richiesta");

            QueueConnection qconn=qconnf.createQueueConnection();
            qconn.start();

            QueueSession qSession=qconn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver qReceiver=qSession.createReceiver(queueRequest);

            Coda coda=new CodaWrapperSynch(new CodaCircolare(10));

            qReceiver.setMessageListener(new ServerListener(coda, qconn));

            System.out.println("[Magazzino] Server avviato");

            while (true) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    break;
                }
            }

            qconn.close();

        }catch(NamingException e){
            e.printStackTrace();
        }catch(JMSException e) {
            e.printStackTrace();
        }

    }
        
}