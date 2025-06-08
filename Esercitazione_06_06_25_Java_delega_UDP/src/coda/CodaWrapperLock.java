package coda;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CodaWrapperLock extends CodaWrapper{
    private Lock lock;
    private Condition empty;
    private Condition full;

    public CodaWrapperLock(Coda c){
        super(c);
        this.lock=new ReentrantLock();
        this.empty=lock.newCondition();
        this.full=lock.newCondition();
    }

    @Override
    public void inserisci(int i) {
        this.lock.lock();

        try{
            while(this.coda.full()){
                try {
                    this.empty.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            this.coda.inserisci(i);
            this.full.signal();
        }finally{
            lock.unlock();
        }
    }

    @Override
    public int preleva() {
        int x=0;
        this.lock.lock();
        try{
            while (this.coda.empty()) {
                try {
                    this.full.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }                
            }
            x=this.coda.preleva();
            this.empty.signal();
        }finally{
            this.lock.unlock();
        }
        return x;
    }
}
