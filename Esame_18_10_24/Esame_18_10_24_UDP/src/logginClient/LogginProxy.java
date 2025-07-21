package logginClient;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

import logginService.ILogging;

public class LogginProxy implements ILogging{

    private String addr;
    private int port;
    private DatagramSocket socket;

    public LogginProxy(String addr, int port){
        this.addr=addr;
        this.port=port;
        try {
            this.socket=new DatagramSocket();
        } catch (SocketException e) {
            e.printStackTrace();
        }
    } 

    @Override
    public void log(String string, int i) {
        
        String msg=new String(string+"-"+Integer.valueOf(i));

        try {
            DatagramPacket request=new DatagramPacket(msg.getBytes(), msg.getBytes().length,InetAddress.getByName(addr),port);

            socket.send(request);

            byte[] buffer=new byte[65508];
            DatagramPacket response=new DatagramPacket(buffer, buffer.length);

            socket.receive(response);
            String res=new String(response.getData(),0,response.getLength());

            System.out.println("[LogginProxy] - Received: "+res);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}
