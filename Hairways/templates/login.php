<?php
session_start();
?>
<!DOCTYPE html>
{% load staticfiles %}
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>
		Salon and spa management Software
	</title>

	<meta name="viewport" content="width=device-width, initial-scale=1"/>

	<link rel="stylesheet" type="text/css" href="{% static 'css/salon-style.css' %}">    <!-- adding css styling -->
	<link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap/css/bootstrap.css' %}">
	<link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap/css/bootstrap-grid.css' %}">
	<link rel="stylesheet" type="text/css" href="{% static 'css/screen.css' %}">


	<script src="{% static 'css/javascript/jquery.js' %}"></script>
	<script src="{% static 'css/javascript/jquery.validate.js' %}"></script>
	<script src="{% static 'css/bootstrap/js/bootstrap.js' %}"></script>
</head>
<body>

	<style>
	html{
		background-image: url("../static/css/images/cover.jpg");
		background-repeat: no-repeat;
		background-size: cover;
		height: 100%;
		width: 100%;
	}
	#commentForm {
		width: 500px;
	}
	#commentForm label {
		width: 250px;
	}
	#commentForm label.error, #commentForm input.submit {
		margin-left: 253px;
	}
	#signupForm {
		width: 600px;
	}
	#signupForm label.error {
		margin-left: 235px;
		width: auto;
		display: inline;
	}
	#newsletter_topics label.error {
		display: none;
		margin-left: 103px;
	}
	</style>


	<div class="container-fluid">
		<div class="sign-container">
			<div class="sign-in" id="sign-in">	  <!-- SIGN IN -->

				<form style="margin-top: 40px" method="POST" action="dashboard/">
					<h1 style="color: green; margin: 0px 0px 0px 0px; text-align: center;">Sign In</h1>
					<input type="text" name="signinuser" placeholder="Username" required>
					<input type="text" name="signinpass" placeholder="Password" required style="margin-top: 80px;" id="password">
					<button type="submit" name="signin" style="position: absolute; margin: 150px 0px 50px 0px; left: 20%; width: 50%; opacity: none; border-radius: 20px;" class="btn btn-success">Sign In</button>
					<a style="position: absolute; bottom: 20px; left: 30px" href="forgot/">Forgot password</a>
				</form>
				<!-- Sign up button on login screen -->
				<button id="br" style="position: absolute; left: 30%; width: 32%; opacity: none; margin: 230px 0px 50px 0px; border-radius: 20px;" class="btn btn-primary" onclick="document.getElementById('sign-up').style.transform= 'perspective( 600px ) rotateY( -180deg )'; document.getElementById('sign-up').style.transform= 'perspective( 600px ) rotateY( 0deg )'; document.getElementById('sign-in').style.visibility= 'hidden'; ">Create account</button>


			</div>

			<!-- Sign up -->
			<div class="sign-up" id="sign-up">
				<div id="main">
					<form class="cmxform" id="signupForm" method="post" action="verify.php">

						<legend style="text-align: center;">Sign Up</legend>
						<p>
							<label for="firstname">First name</label>
							<input id="firstname" name="firstname" type="text">
						</p>
						<p>
							<label for="lastname">Last name</label>
							<input id="lastname" name="lastname" type="text">
						</p>
						<p>
							<label for="username">Username</label>
							<input id="username" name="username" type="text">
						</p>
						<p>
							<label for="password">Password</label>
							<input id="signup_password" name="password" type="password">
						</p>
						<p>
							<label for="confirm_password">Confirm password</label>
							<input id="confirm_password" name="confirm_password" type="password">
						</p>
						<p>
							<label for="email">Email</label>
							<input id="email" name="email" type="email">
						</p>

						<p>
							<input class="submit btn btn-primary" name="signup" type="submit" value="Sign Up" style="text-align: center; background-color: #0069D9; height: 35px; border-radius: 5px; color: white;  margin-top: 30px">
						</p>

					</form>



				</div>
			</div>
		</div>

		<script>
		$.validator.setDefaults({
			submitHandler: function() {
				header("Location: verify.php");
			}
		});

		$().ready(function() {
			// validate the comment form when it is submitted
			$("#commentForm").validate();

			// validate signup form on keyup and submit
			$("#signupForm").validate({
				rules: {
					firstname: "required",
					lastname: "required",
					username: {
						required: true,
						minlength: 2
					},
					password: {
						required: true,
						minlength: 5
					},
					confirm_password: {
						required: true,
						minlength: 5,
						equalTo: "#signup_password"
					},
					email: {
						required: true,
						email: true
					},
				},
				messages: {
					firstname: "Enter your firstname",
					lastname: "Enter your lastname",
					username: {
						required: "Enter a username",
						minlength: "At least 2 characters"
					},
					password: {
						required: "Provide a password",
						minlength: "Must be at least 5 characters long"
					},
					confirm_password: {
						required: "Provide a password",
						minlength: "Must be at least 5 characters long",
						equalTo: "Passwords don't match"
					},
					email: "Enter a valid email address",
				}
			});

			// propose username by combining firstname and lastname
			$("#username").focus(function() {
				var firstname = $("#firstname").val();
				var lastname = $("#lastname").val();
				if (firstname && lastname && !this.value) {
					this.value = firstname + "_" + lastname;
				}
			});

		});
		</script>
	</div>
</body>
</html>
