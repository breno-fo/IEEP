import java.util.Scanner;

public class Main(){
    public static void main(String[] args){
        Alunos a1 = new Alunos();
        Scanner scan = new Scanner(System.in);

        System.out.print("campo do nome: ");
        String nome = scan.nextLine();

        System.out.println("nome final: " + nome);

    }
}