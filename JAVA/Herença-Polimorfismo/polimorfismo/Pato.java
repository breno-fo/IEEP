package polimorfismo;

public class Pato extends Animal{
    @Override
    public void emitirSom(){
        System.err.println(nome + " falando quak..");
    } 
}
