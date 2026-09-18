import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {
        UsuarioComum user = new UsuarioComum();

        user.setEmail(JOptionPane.showInputDialog(null, "Campo de email: "));
        user.setSenha(JOptionPane.showInputDialog(null, "Campo de senha: "));
        user.setTipo(1);

        if (user.logar(user.getEmail(), user.getSenha()) == 0) {
            JOptionPane.showMessageDialog(null, "LOGIN DEU CERTO");
        }else{
            JOptionPane.showMessageDialog(null, "LOGIN FALHOU");
        }

    }
}