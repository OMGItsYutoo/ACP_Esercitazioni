package server;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

import dispatcher.IDispatcher;

public class ServerThread extends Thread{
    
    private Socket socket;
    private IDispatcher ref;

    public ServerThread(Socket s, IDispatcher ref){
        this.socket=s;
        this.ref=ref;
    }

    public void run(){
        System.out.println("[ServerThread] - Thread running!");

        try {
            DataInputStream dataIn=new DataInputStream(new BufferedInputStream(this.socket.getInputStream()));
            DataOutputStream dataOut=new DataOutputStream(new BufferedOutputStream(this.socket.getOutputStream()));

            String method=dataIn.readUTF();

            if(method.compareTo("sendCmd")==0){
                int x=dataIn.readInt();

                System.out.println("[ServerThread] - Received method: "+method);

                this.ref.sendCmd(x);
                dataOut.writeUTF("ack");
            }else if (method.compareTo("getCmd")==0){
                System.out.println("[ServerThread] - Received method: "+method);

                int x=this.ref.getCmd();
                dataOut.writeInt(x);
            }else{
                System.out.println("[ServerThread] - Method not recognized!");
                dataOut.writeUTF("failed");
            }
            dataOut.flush();
            dataIn.close();
            dataOut.close();
            this.socket.close();
            System.out.println();
        } catch (IOException e) {
            System.out.println("Exception: "+e.getMessage());
        }
    }
}
