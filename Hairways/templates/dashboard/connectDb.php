<?php 
	
	$conn = mysqli_connect("localhost","root","","hairways_hairways");

	if(!$conn){
		die("Connection failed: " . mysqli_connect_error());
	}
	else{
		echo "Connected";
	}
?> 