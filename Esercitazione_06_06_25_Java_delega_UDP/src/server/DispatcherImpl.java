package server;

import coda.CodaCircolare;
import coda.CodaWrapper;
import coda.CodaWrapperLock;
import dispatcher.IDispatcher;

public class DispatcherImpl implements IDispatcher{

    private CodaWrapper codaWrapper;

    public DispatcherImpl(int size){
        CodaCircolare c=new CodaCircolare(size);
        codaWrapper=new CodaWrapperLock(c);
    }

    @Override
    public void sendCmd(int command) {
        System.out.println("[DispatcherImpl] - sendCmd "+command);
        codaWrapper.inserisci(command);
    }

    @Override
    public int getCmd() {
        int command=codaWrapper.preleva();
        System.out.println("[DispatcherImpl] - getCmd "+command);

        return command;
    }
    
}
