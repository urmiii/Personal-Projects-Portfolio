<!DOCTYPE html>
<html>
<body>
<link rel="stylesheet" type="text/css" href="signup.css">

<div class="main">

<?php include 'header.php';?>


<div id="container" >  
  <h1 class="one">SIGN</h1>
  <h1 class="two">UP</h1>
</div>


<?php 
$con = mysqli_connect("localhost","root","","trial");
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
if(isset($_POST['bride1']) && isset($_POST['groom1']) && isset($_POST['phone1']) && isset($_POST['email1']) && isset($_POST['username1']) && isset($_POST['password1']))
{
  $newpwd = md5($_POST['password1']);
$query = "INSERT INTO registration(bname, gname, num, email, uname, pwd) VALUES('$_POST[bride1]','$_POST[groom1]','$_POST[phone1]','$_POST[email1]','$_POST[username1]','$newpwd')";
if (mysqli_query($con, $query)) 
{
echo "";
} else {
echo "Error: " . $sql . "<br>" . mysqli_error($con);
}
}

?>


<form name="myForm"   method="post">
  <div class="col-2">
    <label>
      Bride Name
      <input placeholder="What is Bride's First Name?" tabindex="1" name="bride1" required/>
    </label>
  </div>
  <div class="col-2">
    <label>
      Groom Name
      <input placeholder="What is Groom's First Name?" tabindex="2" name="groom1" required/>
    </label>
  </div>
  <div class="col-3">
    <label>
      Phone
      <input placeholder="What is your phone number?" tabindex="3" name="phone1" required/>
    </label>
  </div>
  <div class="col-3">
    <label>
      Email
      <input placeholder="What is the your email address?" tabindex="4" name="email1" required/>
    </label>
  </div>
    <div class="col-4">
    <label>
  Username
      <input placeholder="Enter a Username" tabindex="4" name="username1" required/>
    </label>
  </div>
      <div class="col-5">
    <label>
  Password
      <input placeholder="Enter password" tabindex="4" type="password" name="password1" required/>
    </label>
  </div>
  <div class="button">
  	    <input type="submit" value="Signup" style="color: black;">
  </div>
</form>
</body>
</html>