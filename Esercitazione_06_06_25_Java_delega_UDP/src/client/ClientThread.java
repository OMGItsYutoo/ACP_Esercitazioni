package client;

import java.util.Random;

public class ClientThread extends Thread{

    private DispatcherProxy proxy;
    private static final int NUM_REQS=3;

    public ClientThread(String ip_addr,int port){
        this.proxy=new DispatcherProxy(port, ip_addr);
    }

    public void run(){
        Random rand=new Random();

        for(int i=0;i<NUM_REQS;i++){
            int wait=rand.nextInt(3)+2;

            try {
                Thread.sleep(wait*1000);
            } catch (InterruptedException e) {
                System.out.println("[ClientThread] - Exception: "+e.getMessage());
            }

            int command=rand.nextInt(4);

            System.out.println("[ClientThread] - Sending command: "+command);

            proxy.sendCmd(command);
        }

        
    }
}
