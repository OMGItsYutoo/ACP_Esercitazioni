package client;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

public class Actuator {
    public static void main(String[] args) {
        String ip_addr=args[0];
        int port=Integer.valueOf(args[1]);

        DispatcherProxy proxy=new DispatcherProxy(port, ip_addr);
        int cmd=0;
        PrintStream outStream=null;
        try{
            FileOutputStream fileOut=new FileOutputStream ( "./cmdlog.txt");
			outStream=new PrintStream ( fileOut );
            while (true) {
                cmd=proxy.getCmd();

                System.out.println("[Actuator] - Received command: "+cmd);
                outStream.println("command: "+cmd);
                
                Thread.sleep(1000);
            }
        } catch (IOException e) {
            System.out.println("[Actuator] - Exception: "+e.getMessage());
        } catch (InterruptedException e) {
            System.out.println("[Actuator] - Exception: "+e.getMessage());
        } finally{
            outStream.close();
        }
        
    }
}
