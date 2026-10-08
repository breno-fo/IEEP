<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="liberacao.php" method="post">
        <!-- SELEÇÃO DE CURSO -->
        <select name="curso">
            <option value="segtrab">Segurança do Trabalho</option>
            <option value="devsis">Desenvolvimento de Sistemas</option>
            <option value="nutri">Nutrição e Dietética</option>
            <option value="sec">Secretaria Escolar</option>
        </select>
        
        <!-- SELEÇÃO DE TURNO -->
        <select name="turno">
            <option value="t">Tarde</option>
            <option value="n">Noite</option>
        </select>

        <!-- COLETANDO CREDENCIAL PRO PREENCHIMENTO DO FORMULÁRIO -->
        <input type="password" name="cpf">
        <input type="text" name="cpf" id="cpf" class="cpf" maxlength="11" required>

        <!-- BOTAO DE ENVIO -->
         <button type="submit"> Finalizar Questionário </button> 
    </form>

    <!-- JAVASCRIPT PART -->
    <script>
        /* MASCARA PRA CPF */
        // COLOCANDO PONTOS E TRAÇO
        var cpf = document.querySelector('#cpf');

        cpf.addEventListener("blur", function(){
            if (cpf.value) cpf.value = cpf.value.match(/.{1,3}/g).join(".").replace(/\.(?=[^.]*$)/,"-");
            document.getElementById('aaaa').innerHTML = cpf.value;
        });    

    </script>

</body>
</html>