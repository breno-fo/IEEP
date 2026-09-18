package exemplo2;

public class Main {
    public static void main(String []args){
        Aluno a1 = new Aluno();

        a1.setNome("Breno");
        a1.setMatricula("202207040047");
        
        String nomeAluno = a1.getNome();
        String matAluno = a1.getMatricula();

        System.out.println("o nome do aluno é " + nomeAluno + ", nº de matricula: " + matAluno);
    }
}
