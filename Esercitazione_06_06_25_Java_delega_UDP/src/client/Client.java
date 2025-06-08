package client;

public class Client {
    public static void main(String[] args) {
        /*
		 * uso: 		java client.Client IP porta
		 * per es.:		java client.Client 127.0.0.1 8000
		 */

        String ip_addr=args[0];
        int port=Integer.valueOf(args[1]);

        ClientThread threads[]=new ClientThread[5];
        for(int i=0;i<5;i++){
            threads[i]=new ClientThread(ip_addr,port);
            threads[i].start();
            System.out.println("[Client] - Thread "+i+" started");
        }

        System.out.println("[Client] - Waiting for thread termination");

        for(int i=0;i<5;i++){
            try {
                threads[i].join();
            } catch (InterruptedException e) {
                System.out.println("[Client] - Exception: "+e.getMessage());
            }
        }
    }
}
