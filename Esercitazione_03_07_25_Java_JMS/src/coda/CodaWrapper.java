package coda;

public abstract class CodaWrapper implements Coda{

    protected Coda coda;

    public CodaWrapper(Coda c){
        coda=c;
    }

    @Override
    public boolean empty() {
        return this.coda.empty();
    }

    @Override
    public boolean full() {
        return this.coda.full();
    }

    @Override
    public int getSize() {
        return this.coda.getSize();
    }

}
