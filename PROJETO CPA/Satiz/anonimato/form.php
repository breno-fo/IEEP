<?php
    session_start();
    
    if(!empty($_SESSION["id"])){
        echo "
            <script>
                alet('bem vindo!');
            </script>
        ";
    }else{
        header('location: identificacao.php');
    }
?>