package logginClient;

import java.util.Random;

public class Service {

    private static final int N_REQS=10;
    private static final String[] ERROR_MSGS={"fatal","exception"};
    private static final String[] DBG_INFO_MSGS={"success","checking"};

    public static void main(String[] args) {

        if(args.length!=1){
            System.out.println("[Service] - Please insert the port the server is listening on.");
            System.exit(1);
        }

        int port=Integer.valueOf(args[0]);

        LogginProxy proxy=new LogginProxy("localhost", port);

        for(int i=0; i<N_REQS;i++){
            
            Random ran=new Random();
            
            int tipo=ran.nextInt(3);
            
            String messaggioLog=null;
            
            if(tipo==2) messaggioLog=new String(ERROR_MSGS[ran.nextInt(ERROR_MSGS.length)]);
            else messaggioLog=new String(DBG_INFO_MSGS[ran.nextInt(DBG_INFO_MSGS.length)]);

            proxy.log(messaggioLog, tipo);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        
    }
}
