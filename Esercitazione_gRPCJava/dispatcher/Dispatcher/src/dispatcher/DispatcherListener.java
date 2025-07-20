package dispatcher;

import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;
import javax.jms.TextMessage;

public class DispatcherListener implements MessageListener{
    private QueueConnection qConnection;
    private MagazzinoGrpc.MagazzinoBlockingStub stub;

    public DispatcherListener(QueueConnection qConnection, MagazzinoGrpc.MagazzinoBlockingStub stub){
        this.qConnection=qConnection;
        this.stub=stub;
    }

    @Override
    public void onMessage(Message message) {
        TextMessage textMessage=(TextMessage) message;

        DispatcherThread th=new DispatcherThread(qConnection, stub, textMessage);
        th.start();
    }

    
}
