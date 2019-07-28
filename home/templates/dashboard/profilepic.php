<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>

<style>
  img{
    width: 100px;
    height: 100px;
    max-width: 100px;
    max-height: 100px;
  }
</style>

<body>

  <form action="pic.php" method="post" enctype="multipart/form-data">
    
    <input type="file" name="file">
    <input type="submit" name="submit" value="Upload">
</form>

</body>
</html>

<?php

session_start();

error_reporting(0);
// Include the database configuration file
include 'picconfig.php';


// File upload path
$targetDir = "uploads/";
$fileName = basename($_FILES["file"]["name"]);
$targetFilePath = $targetDir . $fileName;
$fileType = pathinfo($targetFilePath,PATHINFO_EXTENSION);

if(isset($_POST["submit"]) && !empty($_FILES["file"]["name"])){
    // Allow certain file formats
    $allowTypes = array('jpg','png','jpeg','gif','pdf');
    if(in_array($fileType, $allowTypes)){
        // Upload file to server
        if(move_uploaded_file($_FILES["file"]["tmp_name"], $targetFilePath)){
            // Insert image file name into database

            $sql ="UPDATE `hairways`.`salonproducts` SET `product` = '$product', `sold` = '$sold', `price` = '$price', `itemproductsales` = '$itemproductsales' WHERE `salonproducts`.`product` = '$duct'";



            $insert = $db->query("UPDATE salonist SET (username, file_name, uploaded_on) VALUES ('$username', ".$fileName."', NOW())");
            if($insert){
                
                echo "<script type='text/javascript'>alert('The file ".$fileName. " has been uploaded successfully.');</script>";
            }else{
               
                echo "<script type='text/javascript'>alert('File upload failed, please try again.');</script>";
            } 
        }else{
            
            echo "<script type='text/javascript'>alert('Sorry, there was an error uploading your file.');</script>";
        }
    }else{
        
        echo "<script type='text/javascript'>alert('Sorry, only JPG, JPEG, PNG, GIF, & PDF files are allowed to upload.');</script>";
    }
}else{
   
    echo "<script type='text/javascript'>alert('Please select a file to upload.');</script>";
}

// Display status message

?>

<?php

// Include the database configuration file
include 'picconfig.php';

session_start();



// Get images from the database
$query = $db->query("SELECT * FROM images WHERE file_name = '$fileName'");

if($query->num_rows > 0){
    while($row = $query->fetch_assoc()){
        $imageURL = 'uploads/'.$row["file_name"];

?>  
    
    <img src="<?php echo $imageURL; ?>" alt="" />
<?php }
}else{ ?>
    <p>No image(s) found...</p>
<?php } 

?>
