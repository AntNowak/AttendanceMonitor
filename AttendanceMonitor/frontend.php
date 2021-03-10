<?php
session_start();

require_once(dirname(dirname(__FILE__)) . '/htdocs/conf.php');

$dal = new DAL();
?>
<!DOCTYPE html>
<html lang ="en">
<head>
<link rel="stylesheet" type="text/css" href="style1.css">
<title> Register </title>
</head>

<body>

<h2> </h2>
<!--creates box around login textboxes-->
<div class="login-container" id="form">
    <center>
        <br>
        <form action="loginUser.php" method="POST"> <!--POST used due to the login details being sensitive data -->
            <label for="username">Username</label><br>
            <input type="text" placeholder="Your Username..." name="username" id="username"/>
            <br><br>
            <label for="password">Password</label><br>
            <input type="password" placeholder="Your Password..." name="password" id="password"/>
            <br><br><button type="submit" name="submit"><b><i>Login</i></b></button>
        </form>
    </center>


</body>
</html>



