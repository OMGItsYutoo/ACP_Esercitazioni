package checkers;

import java.io.FileWriter;
import java.io.IOException;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;

public class InfoListener implements MessageListener {

    @Override
    public void onMessage(Message message) {
        MapMessage msg=(MapMessage) message;        
        
        try {
            String messaggioLog=new String(msg.getString("messaggioLog"));
            int tipo=msg.getInt("tipo");

            System.out.println("[InfoListener] - Received: "+messaggioLog+", tipo: "+tipo);

            if(tipo==1){
                FileWriter writer=new FileWriter("./src/checkers/info.txt", true);
                writer.write(messaggioLog+"\n");
                writer.close();
            }
        } catch (JMSException | IOException e) {
            e.printStackTrace();
        }
    }
    
}
