package server;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import dispatcher.IDispatcher;

public class DispatcherSkeleton implements IDispatcher{

    private IDispatcher delegate;
    private int port;
    
    public DispatcherSkeleton(int port,IDispatcher delegate) {
        this.delegate = delegate;
        this.port=port;
    }

    public void runSkeleton(){
        
        try{
            ServerSocket socket = new ServerSocket(this.port);
            System.out.println("[DispatcherSkeleton] - Server listening on port: "+this.port);
            
            while (true) {
                Socket s=socket.accept();
                ServerThread t=new ServerThread(s,this);
                t.start();
            }
        }catch(IOException e ){
            System.out.println("Exception: "+e.getMessage());
        }
    }

    @Override
    public void sendCmd(int command) {
        this.delegate.sendCmd(command);
    }

    @Override
    public int getCmd() {
        return this.delegate.getCmd();
    }
    
}
