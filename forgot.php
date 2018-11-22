<!DOCTYPE html>
<html>
<head>
	<title></title>

	<meta name="viewport" content="width=device-width, initial-scale=1"/>
		
	<link rel="stylesheet" type="text/css" href="salon-style.css">    <!-- adding css styling -->
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap-grid.css">
	<link rel="stylesheet" type="text/css" href="fontawesome/fontawesome.css">
	<link rel="stylesheet" type="text/css" href="css/screen.css">

	<script src="javascript/jquery.js"></script>
	<script src="javascript/jquery.validate.js"></script>
	<script src="bootstrap/js/bootstrap.js"></script>
</head>
<body>

	<div class="container-fluid">
	 <div class="sign-container" style="height: 200px">
	 	<div class="sign-in" id="sign-in" style="background-color: whitesmoke">	  
	 		
	 		<form style="margin-top: 40px" method="POST" action="dashboard/dashboard.php">
	 			
	 			<input type="email" name="signinuser" placeholder="Email address" required style="position: absolute; left: 20%;">
	 			
	 			<button type="submit" name="signin" style="position: absolute; margin: 100px 0px 50px 0px; left: 25%; width: 50%; opacity: none; border-radius: 20px;" class="btn btn-success">Reset Password</button>
	 			
	 		</form>
	 	</div>
	 </div>
	</div>
</body>
</html>