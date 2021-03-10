<?php
session_start();
include('logincheck.php'); //checks user is logged in

$sec = 150;
$page =$_SERVER['PHP_SELF'];

require_once(dirname(dirname(__FILE__)) . '/htdocs/conf.php');
$dal = new DAL();
?>

<!DOCTYPE html>
<html lang ="en">
<head>
<script> //Automatic page refresh
function timeRefresh(timeoutPeriod){
    setTimeout("location.reload(true);", timeoutPeriod)
}
windows.onload = timedRefresh(180000); //every 3 minutes
</script>
<!--<meta http-equiv="refresh" content="<!?php echo $sec?>;URL='<!?php echo $page?>'"> --><!--refreshes the page-->
<link rel="stylesheet" type="text/css" href="style2.css"> <!--includes css file-->
<title> Register </title>
</head>
<body>

<!--nav bar-->
<ul>
  <li><a class="active" href="#Home">Home</a></li>
  <li><a href="lectures.php">Lectures</a></li>
  <li style="float:right"><a href="signout.php">Logout</a></li>
</ul>

<!--allows the creation of another box surrounding the welcome text -->
<div class="head"> 
<h1> 
<?php echo ('Welcome back, ' .$dal -> getUser($_SESSION['User']));
     ?></h1>
</div>

<!--splits the remaining page into two columns-->
<br><br><br>
<div class="homeColumn">
        <h1>text</h1>
</div>
</body>
</html>


