package server;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;

import coda.Coda;

public class ServerThread extends Thread{

    private MapMessage mm;
    private Coda coda;
    private QueueConnection qconn;

    public ServerThread(MapMessage m, Coda coda, QueueConnection qconn){
        this.mm=m;
        this.coda=coda;
        this.qconn=qconn;
    }

    @Override
    public void run() {
        try {
            String op = mm.getString("operation");

            if(op.compareTo("deposita")==0){
                int val=mm.getInt("value");
                coda.inserisci(val);
                System.out.println("[ServerThread] - Added "+val+" to queue");
            }else if(op.compareTo("preleva")==0){
                int val=coda.preleva();

                /*
				 * Attenzione, la sessione la devo creare dentro il Thread perchè la session 
				 * è sempre single-threaded. Se creassi la sessione fuori il thread potrei
				 * avere problemi di concorrenza
 				*/

                QueueSession qSession=qconn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

                QueueSender qSender=qSession.createSender((Queue) mm.getJMSReplyTo());
                
                MapMessage reply=qSession.createMapMessage();

                reply.setString("operation", "risultato");
                reply.setInt("value", val);

                qSender.send(reply);

                qSender.close();
                qSession.close();
            }

        } catch (JMSException e) {
            e.printStackTrace();
        }

        
    }
    
}
