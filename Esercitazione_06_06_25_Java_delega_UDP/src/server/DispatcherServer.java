package server;

public class DispatcherServer {
    private static final int queue_size=5;
    private static final int port=7878;
    public static void main(String[] args) {
        System.out.println("[DispatcherServer] Server started ... ");
        DispatcherImpl dispatcherImpl=new DispatcherImpl(queue_size);
        DispatcherSkeleton dispatcherSkeleton=new DispatcherSkeleton(port, dispatcherImpl);
        dispatcherSkeleton.runSkeleton();
    }
}
