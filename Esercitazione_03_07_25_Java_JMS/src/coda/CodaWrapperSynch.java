package coda;

public class CodaWrapperSynch extends CodaWrapper{

    public CodaWrapperSynch(Coda coda) {
        super(coda);
    }

    @Override
    public void inserisci(int i) {
        synchronized(coda){
            while(coda.full()){
                try {
                    coda.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            coda.inserisci(i);
            coda.notifyAll();
        }
    }

    @Override
    public int preleva() {
        int item=0;
        synchronized(coda){
            while(coda.empty()){
                try {
                    coda.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            item=coda.preleva();
            coda.notifyAll();
        }
        return item;
    }
    
}
