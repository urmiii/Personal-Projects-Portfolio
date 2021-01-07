<!DOCTYPE html>
<html>
<title>LOG IN</title>
<body>
  <link rel="stylesheet" type="text/css" href="LOGIN.css">
 <!-- <script>
    function validateForm() {
      var x = document.forms["myForm"]["uname"].value;
      if (x == "") {
        alert("Enter username");
        return false;
      }
      var y = document.forms["myForm"]["pwd"].value;
      if (y == "") {
        alert("Enter password");
        return false;
      }
    }
  </script>-->
 <!-- /**************************************DB**************************************/    -->
<?php     
     $con = mysqli_connect("localhost","root","","trial");
if (mysqli_connect_errno()) 
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


if(isset($_POST['name']) && isset($_POST['password']) ){
$newpwd = md5($_POST['password']);
$query = "INSERT INTO userpass(user, pass) VALUES('$_POST[name]','$newpwd')";
if (mysqli_query($con, $query)) 
{
 header("Location: oindex.php");
} else {
echo "Error: " . $sql . "<br>" . mysqli_error($con);
}
}

?>
<!--
/***********************************SC*****************/-->

<?php

if(isset($_POST['name']) && $_POST['password']!=""){
   $pwd = $_POST['password'];
$con = mysqli_connect("localhost","root","","trial");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

$sql="SELECT * FROM registration WHERE uname='$_POST[name]'";
$result=mysqli_query($con,$sql);

$row=mysqli_fetch_array($result,MYSQLI_ASSOC);
$dbpwd = $row['pwd'];

if(($pwd)==$dbpwd)
{
   //echo "Password match";
   session_start();
   $_SESSION['name']=$row['uname'];

   header("Location: oindex.php");
}
else
{
     header("Location: signup.php");

}


}
?>


  <!-----------------------------------------------NAVIGATION BAR----------------------------------------------------->
  <div class="main">
    <?php include 'header.php';?>


    <!-----------------------------------------------------LOG IN----------------------------------------------------->
    <div id="container">  
      <h1 class="one">LOG</h1>
      <h1 class="two">IN</h1>
    </div>

    <!-----------------------------------------------FORM------------------------------------------------------------->
<form name="myForm" action=#" method="post">
    <label>
        <input type="text"  name="name" required/>
        <div class="label-text" >User name</div>
      </label>
      <label>
        <input type="Password" name="password" required/>
        <div class="label-text">Password</div>
      </label>

<input type="checkbox" name="remember" <?php if(isset($_COOKIE["user"])) { ?> checked <?php }?>/>
<label><div class="label-text" style="font-size: 15px;">Remember me</div></label>

 <button type="submit" name="submit" value="Login" >Submit</button>
<p class="msg"><style type="text/css"> .msg{font-size: 20px;} </style><?php if(isset($msg)) {echo $msg;} ?></p>

        <div>
    <!--Bottom most column in the form-->
    

      <span class="sup" > <a href="Signup.php" style="color: #111; font-size: 12px;">Don't have an account? Sign up </a></span><br>
       <span class="sup" > <a style="color: #111; font-size: 12px;" onclick="popup()"> Forgot Password? </a></span><br>
    </div>
    </form>

<script type="text/javascript">
  function popup(){
var age = parseInt(prompt("Please enter your email address:"));
if(age=""){
  alert("Enter email id")
}
else{
  alert("Thankyou! Please check your email id for the new password")
}
}
</script>

</body>
</html>