import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;
import javax.jms.TextMessage;

public class DispatcherListener implements MessageListener{

    private QueueConnection qConnection;
    private int port;
    private String address;

    public DispatcherListener(QueueConnection qConnection, String address, int port){
        this.qConnection=qConnection;
        this.address=address;
        this.port=port;
    }

    @Override
    public void onMessage(Message message) {
        
        TextMessage mess=(TextMessage) message;

        DispatcherThread t=new DispatcherThread(mess, this.address, this.port, this.qConnection);
        t.start();
    }
    
}
