import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class ServiceProxy implements IService {

    private String address;
    private int port;

    public ServiceProxy(String address, int port){
        this.address=new String(address);
        this.port=port;
    }

    @Override
    public String deposita(int id) {
        String resString=null;
        try {
            Socket s=new Socket(address, port);
            
            /*  NOTE: Un BufferedReader è utilizzato per invocare il metodo readLine, dal momento che le stringhe
			* 	generate lato Python sono terminate con \n, e lato Java la socket si aspetta il terminatore (di default Python non 
			* 	lo aggiunge)
			*/
            DataOutputStream dataOut=new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            BufferedReader dataIn=new BufferedReader(new InputStreamReader(s.getInputStream()));

            dataOut.writeUTF("deposita-"+id);
            dataOut.flush();

            resString = dataIn.readLine();

            System.out.println("[ServiceProxy_Java] - Received result: "+resString);

            dataIn.close();
            dataOut.close();
            s.close();
        } catch (IOException e) {
            System.out.println("[ServiceProxy_Java] - Exception: "+e.getMessage());
        }

        return resString;
    }

    @Override
    public int preleva() {
        int id=-1;
        try {
            Socket s=new Socket(address, port);

            /*  NOTE: Un BufferedReader è utilizzato per invocare il metodo readLine, dal momento che le stringhe
			* 	generate lato Python sono terminate con \n, e lato Java la socket si aspetta il terminatore (di default Python non 
			* 	lo aggiunge)
			*/
            DataOutputStream dataOut=new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            BufferedReader dataIn=new BufferedReader(new InputStreamReader(s.getInputStream()));

            dataOut.writeUTF("preleva");
            dataOut.flush();

            String resString = dataIn.readLine();

            System.out.println("[ServiceProxy_Java] - Received result: "+resString);

            id=Integer.parseInt(resString);

            dataIn.close();
            dataOut.close();
            s.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        return id;
    }
}
