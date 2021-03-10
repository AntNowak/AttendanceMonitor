<?php
session_start();

$username = $_POST["username"];
$password = $_POST["password"];

//finds path for database
require_once(dirname(dirname(__FILE__)) . '\htdocs\conf.php');
$dal = new DAL();

//checks login credential
$check = $dal ->loginUser($username, $password);

if ($check == $username){
    $_SESSION['User'] = $username;
    
    //continues to home page
    header('location: homepage.php');
}
else{
    //goes back to login
    header('location: frontend.php');
}
?>
