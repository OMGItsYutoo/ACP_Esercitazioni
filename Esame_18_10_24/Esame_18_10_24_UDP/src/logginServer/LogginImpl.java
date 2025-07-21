package logginServer;

import javax.jms.*;

public class LogginImpl extends LogginSkeleton {

    private QueueConnection qConnection;
    private Queue errorQueue;
    private Queue infoQueue;

    public LogginImpl(int port, QueueConnection qConnection, Queue errorQueue, Queue infoQueue) {
        super(port);
        this.qConnection=qConnection;
        this.infoQueue=infoQueue;
        this.errorQueue=errorQueue;
    }

    @Override
    public void log(String string, int i) {
        ServerThread t=new ServerThread(string, i, qConnection, errorQueue, infoQueue);
        t.start();
    }
    
}
