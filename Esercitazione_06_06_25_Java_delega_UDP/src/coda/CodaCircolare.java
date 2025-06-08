package coda;

public class CodaCircolare implements Coda {
    private int tail, head, size, elem, data[];

    public CodaCircolare(int s){
        this.size=s;
        elem=0;
        data=new int[this.size];
        tail=head=0;
    }

    @Override
    public void inserisci(int i) {
        data[tail%size]=i;

        try{
			Thread.sleep(101 + (int)(Math.random()*100)  ); //sleep di durata random max pari a 200ms
		}catch ( InterruptedException e ){
			e.printStackTrace();
		}

        elem=elem+1;
        System.out.println("Inserito "+i+" (tot="+elem+")");
        tail=tail+1;
    }

    @Override
    public int preleva() {
        int x = data[ head%size ];

        try{
			Thread.sleep(101 + (int)(Math.random()*400)  ); //sleep di durata random max pari a 500ms
		}catch ( InterruptedException e ){
			e.printStackTrace();
		}
		
		elem=elem-1;
        System.out.println("Prelevato "+x+" (tot="+elem+")");
		
		head=head+1;
		return x;        
    }

    @Override
    public boolean empty() {
        return elem==0;
    }

    @Override
    public boolean full() {
        return elem==size;
    }

    @Override
    public int getSize() {
        return this.size;
    }   
}