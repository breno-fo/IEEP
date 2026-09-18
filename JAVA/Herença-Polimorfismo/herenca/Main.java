package herenca;

public class Main {
    public static void main(String[] args) {
        Cavalo cavalo = new Cavalo();

        cavalo.nome = "Horbison";
        System.out.println("o nome do cavalo é: " + cavalo.nome);
        cavalo.comer();
        cavalo.correr();
        cavalo.cavalar();
    }
}
