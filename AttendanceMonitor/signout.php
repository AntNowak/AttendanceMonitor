<?php
//signs out the user
session_start();
unset($_SESSION['User']);
header('location: frontend.php');

require_once(dirname(dirname(__FILE__)) . '/htdocs/conf.php');
//require_once(dirname(dirname(__FILE__)) . '\htdocs\conf.php');
$dal = new DAL();
?>
