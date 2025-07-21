package logginServer;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

import logginService.ILogging;

public abstract class LogginSkeleton implements ILogging {

    private int port;

    public LogginSkeleton(int port){
        this.port=port;
    }

    public void runSkeleton(){

        try {
            DatagramSocket sock=new DatagramSocket(port);

            System.out.println("[LogginSkeleton] - Waiting for request on port: 12122");

            while(true){

                byte[] buffer=new byte[65508];
                DatagramPacket request=new DatagramPacket(buffer, buffer.length);

                sock.receive(request);

                String str=new String(request.getData(), 0, request.getLength());

                String[] str_split=str.split("-");

                this.log(str_split[0], Integer.valueOf(str_split[1]));

                System.out.println("[LogginSkeleton] - Request satisfied");

                String responseStr=new String("done");
                DatagramPacket response=new DatagramPacket(responseStr.getBytes(), responseStr.getBytes().length, request.getAddress(), request.getPort());

                sock.send(response);
            }

            //sock.close();

        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
