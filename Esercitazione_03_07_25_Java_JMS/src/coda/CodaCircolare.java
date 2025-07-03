package coda;

public class CodaCircolare implements Coda{

    private int items, tail, head, size;
    private int data[];

    public CodaCircolare(int size){
        items=tail=head=0;
        this.size=size;
        data=new int[10];
    }

    @Override
    public void inserisci(int i) {
        data[tail%size]=i;
        items++;
        tail++;
    }

    @Override
    public boolean empty() {
        return items==0;
    }

    @Override
    public boolean full() {
        return items==this.size;
    }

    @Override
    public int getSize() {
        return size;
    }

    @Override
    public int preleva() {
        int item=data[head%size];
        items--;
        head++;
        return item;
    }
    
}
