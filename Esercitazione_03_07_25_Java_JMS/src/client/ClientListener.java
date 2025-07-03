package client;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;

public class ClientListener implements MessageListener {

    @Override
    public void onMessage(Message message) {
        MapMessage mm=(MapMessage) message;

        try {
            System.out.println("[ClientListener] - Received a message from response queue: "+ mm.getInt("value"));
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
    
}
