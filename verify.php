<?php

if(isset($_POST['signup'])) {

  require 'password_hash_compatibilty.php';

  include_once 'connectDb.php';

  $hash = md5(rand(0,9999) );

  // Escape user inputs for security
  $firstname = mysqli_real_escape_string($conn, $_REQUEST['firstname']);
  $lastname = mysqli_real_escape_string($conn, $_REQUEST['lastname']);
  $username = mysqli_real_escape_string($conn, $_REQUEST['username']);
  $email = mysqli_real_escape_string($conn, $_REQUEST['email']);
  $password = mysqli_real_escape_string($conn, $_REQUEST['password']);
  $hash = mysqli_real_escape_string($conn, $hash);

  $sql = "SELECT * FROM salonist WHERE username = '$username'";
   $result = mysqli_query($conn, $sql);
   $resultCheck = mysqli_num_rows($result);
   if($resultCheck > 0){
      header("Location: salonist.php#signup?signup=userexists");
          exit();
   }else{
    $sql = "SELECT * FROM salonist WHERE email = '$email'";
   $result = mysqli_query($conn, $sql);
   $resultCheck = mysqli_num_rows($result);
   if($resultCheck > 0){
      header("Location: salonist.php#sign-up?signup=emailexists");
          exit();
   }else{
      $hashedpass = password_hash($password, PASSWORD_DEFAULT);
   

// Attempt insert query execution
$sql = "INSERT INTO salonist (id ,fname, lname, username, email, pass, registerDate, activatehash, active) VALUES (NULL, '$firstname', '$lastname', '$username', '$email', '$hashedpass', NOW(), '$hash', '0')";

    $to = "$email";              
    $from = "info@hairways.co.ke";
    $subject = 'Hairways Account Activation';
    $message = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>yoursitename Message</title></head><body style="margin:0px; font-family:Tahoma, Geneva, sans-serif;"><div style="padding:10px; background:#333; font-size:24px; color:#CCC;"><a href="http://www.hairways.co.ke">Hairways Account Activation</div><div style="padding:24px; font-size:17px;">Hello '.$username.',<br /><br />Click the link below to activate your account when ready:<br /><br /><a href="http://hairways.co.ke/dashboard/dashboard.php">Click here to activate your account now</a><br /><br />Login after successful activation using your:<br />* E-mail Address: <b>'.$email.'</b></div></body></html>';
    $headers = "From: $from\n";
        $headers .= "MIME-Version: 1.0\n";
        $headers .= "Content-type: text/html; charset=iso-8859-1\n";
    mail($to, $subject, $message, $headers);
    echo "signup_success";
    exit();
  }
  exit();
}







// Close connection
mysqli_close($conn);

  // Returns user to sign up page if submit button was never clicked
}else{
  header("Location: salonist.php");
  exit();
}
 


?>

<!DOCTYPE html>
<html>
<head>
	<title></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.css">
	
</head>
<body>
	<div class="verify" style=" top: 20px; width: 60%; background-color: whitesmoke; position: relative; text-align: center; height: auto; margin: 0 auto; padding: 20px 0px 20px 0px">
		<p>Hi <b style="color: green"><?php echo $_POST["firstname"]; ?></b></p> 
    <p style="padding: 0px 10px 0px 0px">Welcome to Hairways salon management software. An activation link has been sent to: <b style="color: blue"><?php echo $_POST["email"]; ?></b></p>
	
    <button class="btn btn-primary" style="text-align: center; height: 40px; color: #fff; background-color: #00B5D8; margin: 40px 0px 40px 0px; font-weight: bold; padding: 0px 30px 0px 30px;">Verify</button>
  </div>
</body>
</html>


