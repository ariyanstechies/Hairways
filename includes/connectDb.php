<?php 
	
	$conn = mysqli_connect("localhost","root","","hairways");

	if(!$conn){
		die("Connection failed: " . mysqli_connect_error());
	}
	else{
		echo "Success";
	}
?> 