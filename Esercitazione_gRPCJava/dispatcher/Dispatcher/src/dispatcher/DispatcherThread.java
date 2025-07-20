package dispatcher;

import javax.jms.*;

public class DispatcherThread extends Thread{

    private QueueConnection qConnection;
    private MagazzinoGrpc.MagazzinoBlockingStub stub;
    private TextMessage message;

    public DispatcherThread(QueueConnection qConnection, MagazzinoGrpc.MagazzinoBlockingStub stub, TextMessage message){
        this.qConnection=qConnection;
        this.stub=stub;
        this.message=message;
    }

    @Override
    public void run() {
        try {
            String msg=message.getText();

            String result=null;

            if(msg.equalsIgnoreCase("preleva")){
                System.out.println("[DispatcherThread_Java] - Received preleva request");

                Empty empty=Empty.newBuilder().build();

                Item item=stub.preleva(empty);
                result=new String(Long.toString(item.getValue()));
            }else if(msg.contains("deposita")){

                System.out.println("[DispatcherThread_Java] - Received deposita request");
                
                String[] msg_split=msg.split("-");
                int value=Integer.valueOf(msg_split[1]);

                Item item=Item.newBuilder().setValue(value).build();

                stub.deposita(item);
                result=new String("deposited");
            }

            //risposta tramite JMS
            Queue response=(Queue) message.getJMSReplyTo();
            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            TextMessage msg_to_send=qSession.createTextMessage(result);
            QueueSender qSender=qSession.createSender(response);
            qSender.send(msg_to_send);

            qSender.close();
            qSession.close();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
    
}
