<?php
session_start();
$sec = 150;
$page =$_SERVER['PHP_SELF'];

require_once(dirname(dirname(__FILE__)) . '/htdocs/conf.php');
$dal = new DAL();
?>
<!DOCTYPE html>
<html lang ="en">
<head>
<meta http-equiv="refresh" content="150;URL='/homepage.php'"> <!--refreshes the page-->
<link rel="stylesheet" type="text/css" href="style2.css"> <!--includes css file-->
<title> Register </title>
</head>
<body>
<!--creates page navigation bar-->
<div class="navbar">
<a class="active" href="home.php"> Home</a>
<a href="lectures.php">Lectures</a>
<div class="navbar-right"> <!--makes the logout button sit on the right of the screen-->
    <a href="signout.php">Logout</a>
</div>
<!--splits the remaining page into two columns-->
<br><br><br>
<div class="row">
    <div class="column1">
   
    </div>
</div>
</body>
</html>

