<!-----------------------------------------------------PHP------------------------------------------------------------->
<?php

$con = mysqli_connect("localhost","root","","trial");

if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$newpwd = md5($_POST['password1']);

$query = "INSERT INTO tbl_user(bname, gname, num, email, uname, pwd) VALUES('$_POST[bride1]','$_POST[groom1]','$_POST[phone1]','$_POST[email1]','$_POST[username1]','$newpwd')";

if (mysqli_query($con, $query)) 
{
	header("location:login.php");
} else {
echo "Error: " . $sql . "<br>" . mysqli_error($con);
}
?>

