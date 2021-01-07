<!-----------------------------------------------------PHP------------------------------------------------------------->
<?php
$con = mysqli_connect("localhost","root","","trial");
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$newpwd = md5($_POST['pwd']);
$query = "INSERT INTO trialtable(uname, pwd) VALUES('$_POST[uname]','$newpwd')";
if (mysqli_query($con, $query)) 
{
	header("location:login.php");
} else {

echo "Error: " . $sql . "<br>" . mysqli_error($con);
}
?>

