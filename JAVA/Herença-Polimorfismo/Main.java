public class Main{
    public static void main(String[] args) {
        Carros car = new Carros();
        
        car.setModelo("Gol quadrado");
        car.setMarca("Wolksvagem");
        car.setAno(2007);
        car.setVelocidade(100);

        String nome = car.getModelo();
        String marc = car.getMarca();
        int ano = car.getAno();
        float vel = car.getVelocidade();

        System.out.println("a marca do carro é: " + marc);
        System.out.println("o nome do carro é: " + nome);
        System.out.println("o ano é: " + ano);
        System.out.println("a velocidade e: " + vel);
    }
}