package checkers;

import java.io.FileWriter;
import java.io.IOException;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;

public class ErrorListener implements MessageListener{
    
    private String checkerType;

    public ErrorListener(String checkerType){
        this.checkerType=new String(checkerType);
    }

    @Override
    public void onMessage(Message message) {
        MapMessage msg=(MapMessage) message;

        try {
            String messaggioLog=new String(msg.getString("messaggioLog"));

            System.out.println("[ErrorListener] - Received: "+messaggioLog);

            if(messaggioLog.equalsIgnoreCase(checkerType)){
                FileWriter writer=new FileWriter("./src/checkers/error.txt", true);
                writer.write(messaggioLog+"\n");
                writer.close();
            }
        } catch (JMSException | IOException e) {
            e.printStackTrace();
        }
    }
}
