package server;

import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;

import coda.Coda;

public class ServerListener implements MessageListener{

    private Coda coda;
    private QueueConnection qconn;

    public ServerListener(Coda coda, QueueConnection qconn){
        this.coda=coda;
        this.qconn=qconn;
    }

    @Override
    public void onMessage(Message message) {
        MapMessage m=(MapMessage) message;

        ServerThread t=new ServerThread(m, coda, qconn);
        t.start();
    }
    
}
