<?php
    $host = "localhost";
    $dbname = "cp";
    $senha = "";
    $usuario = "root"

    $dns = "mysql:host=".$host.";dbname=".$dbname;

    try {
        $pdo = new PDO($dns, $usuario, $senha);
    } catch (PDOexception $error) {
        echo $error;
    }
?>