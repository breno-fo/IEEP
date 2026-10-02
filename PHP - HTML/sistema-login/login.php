<?php

    include 'connection.php';

    $email = $_POST['userEmail'];
    $password =  sha1($_POST['userPass']);

    $query = "SELECT * FROM users WHERE email = '$email' AND password = '$password';";

    $sql = $pdo->prepare($query);
    $sql->execute($query);

    $result = $sql->rowCount();
    if($result > 0){
        header('location: dashboard.html');    
    } else {
        header('location: erro.html');
    }

?>