public class Carros {
    private String modelo;
    private String marca;
    private int ano;
    private float velocidade;


    public String getModelo(){
        return modelo;
    }
    public String getMarca(){
        return marca;
    }
    public int getAno(){
        return ano;
    }
    public float getVelocidade(){
        return velocidade;
    }


    public void setModelo(String modelo){
        this.modelo = modelo;
    }
    public void setMarca(String marca){
        this.marca = marca;
    } 
    public void setAno(int ano){
        this.ano = ano;
    }
    public void setVelocidade(float velocidade){
        this.velocidade = velocidade;
    }

}
