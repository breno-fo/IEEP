public class Usuario{
    private String email;
    private String senha;
    private int tipo;

    public int logar(String email, String senha){
        if(email.equals("teste@gmail.com") && senha.equals("1234")){
            return 0;
        }else{
            return -1;
        }
    }


    // Encapsulmento -- email
    public String getEmail(){
        return email;
    }
    public void setEmail(String email){
        this.email = email;
    }

    
    // Encapsulmento -- senha
    public String getSenha(){
        return senha;
    }
    public void setSenha(String senha){
        this.senha = senha;
    }


    // Encapsulmento -- tipo
    public int getTipo(){
        return tipo;
    }
    public void setTipo(int tipo){
        this.tipo = tipo;
    }
}