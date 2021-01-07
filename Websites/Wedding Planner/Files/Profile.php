<!DOCTYPE html>
<html>
<head>
	<title>PROFILE</title>
</head>
<body>
	<link rel="stylesheet" type="text/css" href="profile.css">

	<!---------------------------NAVIGATION BAR-------------------->
	<?php include 'header.php';?>

	<!-----------------------------------------------------YOUR PROFILE----------------------------------------------------->
	<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700,800' rel='stylesheet' type='text/css'>

	<div id="container">  
		<h1 class="one">YOUR</h1>
		<h1 class="two"> PROFILE</h1>
	</div>

	<!-----------------------------------------------------FORM------------------------------------------------------------->
	<form action="#">
		<div class="row"   style=" margin-top: 250px;">
			<input type="text" name="fancy-text" id="fancy-text"/>
			<label for="fancy-text">Bride Name</label>
		</div>

		<div class="row">
			<input type="text" name="fancy-text" id="fancy-text"/>
			<label for="fancy-text">Groom Name</label>
		</div>

		<div class="row">
			<input type="text" name="fancy-text" id="fancy-text"/>
			<label for="fancy-text">Email</label>
		</div>

		<div class="row">
			<input type="text" name="fancy-text" id="fancy-text"/>
			<label for="fancy-text">Password</label>
		</div>

		<div class="row">
			<input type="text" name="fancy-text" id="fancy-text"/>
			<label for="fancy-text">Big Date</label>
		</div>

		<button type="submit" tabindex="0">SAVE CHANGES</button>
	</form>
</body>
</html>