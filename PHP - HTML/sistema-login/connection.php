<?php
    $host = "localhost";
    $dbmame = "bd_login";
    $user = "root";
    $password = "";

    $dns = "mysql:host=".$host.";dbname=".$dbmame;

    try {
        $pdo = new PDO($dns, $user, $password);

    } catch (PDOException $error) {
        echo "Erro:".$error;
    }
?>