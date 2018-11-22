<?php 

include_once 'connectDb.php';

if(isset($_POST['updateprofile'])) {

  require 'password_hash_compatibilty.php';

  
  // Escape user inputs for security
  $firstname = mysqli_real_escape_string($conn, $_REQUEST['firstname']);
  $lastname = mysqli_real_escape_string($conn, $_REQUEST['lastname']);
  $username = mysqli_real_escape_string($conn, $_REQUEST['username']);
  $salonName = mysqli_real_escape_string($conn, $_REQUEST['salonName']);
  $salonDescription = mysqli_real_escape_string($conn, $_REQUEST['salonDescription']);
  $salonLocation = mysqli_real_escape_string($conn, $_REQUEST['salonLocation']);
  $email = mysqli_real_escape_string($conn, $_REQUEST['email']);
  $phoneNo = mysqli_real_escape_string($conn, $_REQUEST['phoneNo']);
  $password = mysqli_real_escape_string($conn, $_REQUEST['password']);

      $hashedpass = password_hash($password, PASSWORD_DEFAULT);
   

// Attempt insert query execution
$sql = "INSERT INTO salonist (id ,fname, lname, username,salonName, salonDescription, location, phoneNo, email, pass) VALUES (NULL, '$firstname', '$lastname', '$username', '$salonName', '$salonDescription', '$salonLocation',
 '$email', '$phoneNo', '$hashedpass')";
if(mysqli_query($conn, $sql)){
  echo "data inserted";
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
}
}else{
  echo "FIrst press edit";
  exit();
}
 

 ?>

 <!DOCTYPE html>
 <html>
 <head>
 	<title></title>
 </head>
 <body>
 
 </body>
 </html>