

public class Main{
    public static void main(String[] args){
        // CRIANDO O OBJETO    
        Calc c1 = new Calc();
        
        // EXECUTANDO OS METODOS (SOMA, SUB, MULT, DIV)
        int soma = c1.sum(1,1);
        int subtracao = c1.sub(1,1);
        int multiplicacao = c1.mult(1,1);
        int divisao = c1.div(1,1);

        // EXIBINDO RESULTADOS
        System.out.println("--------------------");
        System.out.println("O resultado final é:");
        System.out.println("Soma: " + soma);
        System.out.println("Subtração: " + subtracao);
        System.out.println("Divisão: " + divisao);
        System.out.println("Multiplicação: " + multiplicacao);
        System.out.println("--------------------");
    }
}