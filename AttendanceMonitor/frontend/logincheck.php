<?php
//checks that the user is actually signed into an accountbefore allowing them access to the page
//and checks the session hasnt ended after a refresh
if(empty($_SESSION['User'])){
	header('location: frontend.php');
}

require_once(dirname(dirname(__FILE__)) . '/htdocs/conf.php');
//require_once(dirname(dirname(__FILE__)) . '\htdocs\conf.php');
$dal = new DAL();
?>
