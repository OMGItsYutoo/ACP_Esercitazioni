package logginServer;

import javax.jms.*;

public class ServerThread extends Thread {

    private String s;
    private int i;
    private QueueConnection qConnection;
    private Queue errorQueue;
    private Queue infoQueue;

    public ServerThread(String s, int i, QueueConnection qConnection, Queue errorQueue, Queue infoQueue){
        super();
        this.s=s;
        this.i=i;
        this.qConnection=qConnection;
        this.infoQueue=infoQueue;
        this.errorQueue=errorQueue;
    }

    public void run(){
        System.out.println("[ServerThread] - Thread running");

        try {
            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            
            MapMessage mm=qSession.createMapMessage();
            
            mm.setString("messaggioLog", s);
            mm.setInt("tipo", i);
            
            QueueSender qSender=null;
            if(i==2){
                qSender=qSession.createSender(errorQueue);
                qSender.send(mm);
            }else{
                qSender=qSession.createSender(infoQueue);
                qSender.send(mm);
            }

            qSender.close();
        } catch (JMSException e) {
            e.printStackTrace();
        }


    }
}
