<?php
    // include 'connection.php';

    $curso = $_POST['curso'];
    $turno = $_POST['turno'];
    $cpf = $_POST['cpf'];

    // DEBUG VISUAL SIMPLES
    echo $curso."<br>".$turno."<br>".$cpf; 

    $query_confirm = "INSERT INTO entrevistados VALUES (NULL, $curso, $turno, $cpf, 1);";
    $sql1 = $pdo->prepare($query_confirm);
    if ($sql1->execute()){
        SESSION_START();
        $_SESSION["id"] = rand(1, 999);
        header("location: form.php");
    }else{
        header("location: identificacao.php");
    }
?>