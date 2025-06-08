package client;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

import dispatcher.IDispatcher;

public class DispatcherProxy implements IDispatcher{
    private int port;
    private String addr;

    public DispatcherProxy(int port, String addr){
        this.port=port;
        this.addr=new String(addr);
    }

    @Override
    public void sendCmd(int command) {
        try {
            Socket sock=new Socket(addr,port);

            DataInputStream dataIn=new DataInputStream(new BufferedInputStream(sock.getInputStream()));
            DataOutputStream dataOut=new DataOutputStream(new BufferedOutputStream(sock.getOutputStream()));

            System.out.println("[DispatcherProxy] - Sending sendCmd with command: "+command);

            dataOut.writeUTF("sendCmd");
            dataOut.writeInt(command);
            dataOut.flush();

            String response=dataIn.readUTF();

            System.out.println("[DispatcherProxy] - Received response "+response);
            dataIn.close();
            dataOut.close();
            sock.close();
        } catch (UnknownHostException e) {
            System.out.println("[DispatcherProxy] - Exception: "+e.getMessage());
        } catch (IOException e) {
            System.out.println("[DispatcherProxy] - Exception: "+e.getMessage());
        }
    }

    @Override
    public int getCmd() {
        int command=0;
        try {
            Socket sock=new Socket(addr,port);

            DataInputStream dataIn=new DataInputStream(new BufferedInputStream(sock.getInputStream()));
            DataOutputStream dataOut=new DataOutputStream(new BufferedOutputStream(sock.getOutputStream()));

            System.out.println("[DispatcherProxy] - Sending getCmd");

            dataOut.writeUTF("getCmd");
            dataOut.flush();
            command=dataIn.readInt();

            System.out.println("[DispatcherProxy] - Received: "+command);

            dataIn.close();
            dataOut.close();
            sock.close();
        } catch (UnknownHostException e) {
            System.out.println("[DispatcherProxy] - Exception: "+e.getMessage());
        } catch (IOException e) {
            System.out.println("[DispatcherProxy] - Exception: "+e.getMessage());
        }
        return command;
    }
    
}
