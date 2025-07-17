import javax.jms.*;

public class DispatcherThread extends Thread {

    private QueueConnection qConnection;
    private TextMessage msg;
    private int port;
    private String address;

    public DispatcherThread(TextMessage msg, String address, int port, QueueConnection qConnection){
        this.msg=msg;
        this.port=port;
        this.qConnection=qConnection;
        this.address=address;
    }

    public void run(){
        try {
            String msgstr=msg.getText();

            System.out.println("[DispatcherMsgListener_Java] - Received: "+msgstr);

            Queue responses=(Queue) msg.getJMSReplyTo();

            IService proxy=new ServiceProxy(address, port);

            String[] msgSplit=msgstr.split("-");

            String result=null;
            if(msgSplit[0].equalsIgnoreCase("preleva")){
                int id=proxy.preleva();

                result=new String(Integer.toString(id));
            }else if(msgSplit[0].equalsIgnoreCase("deposita")){
                int idFromString=Integer.valueOf(msgSplit[1]);

                result=new String(proxy.deposita(idFromString));
            }

            QueueSession qSession=qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueSender qSender=qSession.createSender(responses);

            TextMessage message=qSession.createTextMessage(result);
            qSender.send(message);

            qSender.close();
            qSession.close();
        } catch (JMSException e) {
            System.out.println("[DispatcherMsgListener_Java] - Exception: "+e.getMessage());
        }
    }
}
