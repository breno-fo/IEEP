package polimorfismo;

public class Main {
    public static void main(String[] args) {
        Animal pato = new Pato();
        Animal urso = new Urso();
        Animal aracuara = new Aracuara();
        
        pato.nome = "Patola";
        urso.nome = "Ze Comeia";
        aracuara.nome = "Ararucara";
        
        pato.emitirSom();
        urso.emitirSom();
        aracuara.emitirSom();
    }   
}
