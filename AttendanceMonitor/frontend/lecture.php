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
<!--lad's code for face rec --> 
<!--<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.4/socket.io.js" integrity="sha512-aMGMvNYu8Ue4G+fHa359jcPb1u+ytAF+P2SCb+PxrjCdO3n3ZTxJ30zuH39rimUggmTwmh2u7wvQsDTHESnmfQ==" crossorigin="anonymous"></script>
    <script type="text/javascript" charset="utf-8">
        $(function () {
            // Connect to the Socket.IO server.
            var socket = io();

            // Event handler for server sent data.
            socket.on('state_change', function (msg) {
                $('#state').text(function (i, oldText) {
                    return "Current State: " + msg.new_state;
                });
            });

            // Event handler for server sent data.
            socket.on('image_data', function (msg) {
                $('#img').attr('src', msg.buffer);
               // $('#studentID').text(function (i, oldText) {
                    // return "Student ID: " + msg.student_id
                });
                $('#confidence').text(function (i, oldText) {
                     return "Distance (lower the better): " + msg.confidence
                });
            });
        });
    </script> --><!--end of lad's code-->
</head>
<body>

<!--creates page navigation bar-->
<div class="navbar">
<a href="homepage.php"> Home</a>
<a class="active" href="lecture.php">Lectures</a>
<div class="navbar-right"> <!--makes the logout button sit on the right of the screen-->
    <a href="signout.php">Logout</a>
</div>


<!--splits the remaining page into two columns-->
<br><br><br>
<div class="row">
    <div class="column1">
    <!--shows image data
    <h2 id="state">
       Current State: face</h2>
           <h2 id="confidence">
               </h2>
            <img id="img" />-->
    </div>
</div>
</body>
</html>

