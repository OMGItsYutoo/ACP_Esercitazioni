import java.io.FileWriter;
import java.io.IOException;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;
import javax.jms.Topic;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;

public class ManagerListener implements MessageListener{

    private TopicSession tSession;
    private Topic statsTopic;
    private Topic ticketsTopic;

    public ManagerListener(TopicSession tSession, Topic statsTopic, Topic ticketsTopic){
        this.tSession=tSession;
        this.ticketsTopic=ticketsTopic;
        this.statsTopic=statsTopic;
    }

    @Override
    public void onMessage(Message message) {
        try {

            MapMessage mm=(MapMessage) message;

            String type=mm.getString("type");    
            String value=mm.getString("value");

            TextMessage msg_to_send=tSession.createTextMessage(value);
            TopicPublisher tPublisher=null;
            if(type.equalsIgnoreCase("stats")){
                tPublisher=tSession.createPublisher(this.statsTopic);
                tPublisher.publish(msg_to_send);
            }else if(type.equalsIgnoreCase("buy")){                
                FileWriter writer=new FileWriter("tickets.txt",true);
                writer.append(value+"\n");
                writer.close();

                tPublisher=tSession.createPublisher(ticketsTopic);
                tPublisher.publish(msg_to_send);
            }

            tPublisher.close();
        } catch (JMSException e) {
            e.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }

    }
    
}
