<!DOCTYPE html>
<html>
<head>
  <title>For the best Salons, Barber shop in town</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  
  <link rel="stylesheet" type="text/css" href="salon-style.css">   
  <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/css/bootstrap-combined.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" media="screen"
     href="http://tarruda.github.com/bootstrap-datetimepicker/assets/css/bootstrap-datetimepicker.min.css">

  <!-- <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.css"> -->
  <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap-grid.css">
  <link rel="stylesheet" type="text/css" href="fontawesome/fontawesome.css">

  <script src="javascript/jquery.js"></script>
  <script src="bootstrap/js/bootstrap.js"></script>
  <script src="javascript/javascript.js"></script>

  <script src="javascript/scroll-horizontal.js"></script>
  <style>
    .form-group input{
      height: 30px;
    }

  </style>

</head>

  <section class="main">      
  
          <div class="content">
               <div class="container-fluid" style="width: 100%">

                <a href="index.html #search-results"><button class="back btn btn-primary" style="margin: 10px 0px 20px 30px;">Back</button></a>
                
              <div class="content">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-7" style="margin-bottom: 30px;">
                      <div class="card">
                        
                        <div class="card-body" style="background-image: url(images/1.jpg); background-size: cover; height: 400px">
                
                        </div>
                      </div>
                    </div>
                    <div class="col-md-5" style="margin-bottom: 30px;">
                   <div class="card card-profile" style="height: 400px" id="map">
                  
                    
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            
                   <div class="content">
                  <div class="container-fluid">
                    <div class="row">
                        <div class="col-md-7" style="margin-bottom: 30px;">
                          <div class="card">
                            
                            <div class="card-body">
                          <div style="background-color: #007BFF" class="card-header card-header-primary">
                              <div class="card-category"><b style="color: #fff; position: absolute; padding: 20px 0px 0px 20px">Services we offer</b></p>
                              </div>
                            </div>
                            </div>

                            <table class="table table-striped">
                          <thead>
                            <tr>
                              <th scope="col">#</th>
                              <th scope="col">Service</th>
                              <th scope="col">Duration(mins)</th>
                              <th scope="col">Cost(kSh)</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td><input type="checkbox" id="check" class="custom-control-input" name="haircut" onclick="myFunction()"></td>
                              <td>Hair cut</td>
                              <td>30</td>
                              <td>100</td>
                            </tr>
                            <tr>
                              <td><input type="checkbox" id="check1" class="custom-control-input" name="haircut" onclick="myFunction1()"></td>
                              <td>Blow dry</td>
                              <td>45</td>
                              <td>300</td>
                            </tr>
                            <tr>
                              <td><input type="checkbox" id="check2" class="custom-control-input" name="haircut" onclick="myFunction2()"></td>
                              <td>Manicure</td>
                              <td>25</td>
                              <td>200</td>
                            </tr>
                          </tbody>
                        </table>

                          </div>
                          </div>
            
                        <div class="col-md-5" style="margin-bottom: 30px; height: auto;">
                            <div class="card card-profile" style="padding: 50px 0px 20px 40px"; >

                              <h5>Services booked for:</h5>

                              <p id="text" style="display:none">Hair cut</p>
                              <p id="text1" style="display:none">Blow dry</p>
                              <p id="text2" style="display:none">Manicure</p>

                            <script>
                              function myFunction() {
                                // Get the checkbox
                                var checkBox = document.getElementById("check");
                                // Get the output text
                                var text = document.getElementById("text");

                                // If the checkbox is checked, display the output text
                                if (checkBox.checked == true){
                                  text.style.display = "block";
                                } else {
                                  text.style.display = "none";
                                }
                              }
                              function myFunction1() {
                                // Get the checkbox
                                var checkBox1 = document.getElementById("check1");
                                // Get the output text
                                var text1 = document.getElementById("text1");

                                // If the checkbox is checked, display the output text
                                if (checkBox1.checked == true){
                                  text1.style.display = "block";
                                } else {
                                  text1.style.display = "none";
                                }
                              }
                              function myFunction2() {
                                // Get the checkbox
                                var checkBox2 = document.getElementById("check2");
                                // Get the output text
                                var text2 = document.getElementById("text2");

                                // If the checkbox is checked, display the output text
                                if (checkBox2.checked == true){
                                  text2.style.display = "block";
                                } else {
                                  text2.style.display = "none";
                                }
                              }
                              </script>



                              <div id="datetimepicker" class="input-append date" style="padding: 30px 0px 50px 0px">

                                  <input id="appointmentTime" style="height: 30px" type="text"></input>
                                  <span class="add-on">
                                    <i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
                                  </span>
                                </div>
                                <div>
                                  
                                  <form>
                                    <div class="form-group">
                                      <label for="name">Name</label>
                                      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter name">
                                      
                                    </div>
                                    <div class="form-group">
                                      <label for="email">Email</label>
                                      <input type="email" class="form-control" id="exampleInputPassword1" placeholder="Email">
                                </div>
                                    
                                    <button type="submit" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-lg">Submit</button>
                                  </form>


                              <script>
                             $(document).ready(function(){
                                $('#booked').click(function() {           
                               $date = $("#datetimepicker").find("input").val();      
                                                 
                                }); 
                            });

                              </script>


                             <div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
                              <div class="modal-dialog modal-lg" role="document">
                                <div class="modal-content">
                                  <div class="modal-header">
                                  <div class="modal-body"> 

                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">&times;</span>
                                    </button>
                                    <div class="appointment" style="height: 300px; text-align: center;">

                                      <h3 style="margin-bottom: 30px; color: blue">Book confirmed</h3>
                               
                                      <h4>Thanks for booking your appointment has been received</h4>

                                      <img src="images/success.png" style="height: 100px; width: 100px; margin: 20px 0px 0px 0px; " align="center">                          
                                      
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                  </div>
                            </div>
                  </div>
               

          
      </section>

      <script>
        function getTime(){
          var date = document.getElementById('Time').value;
           document.getElementById('Time').innerHTML = date;
        }
      </script>

   <!--  Google Maps Plugin    -->
      <script>
// Initialize and add the map
function initMap() {
  // The location of Uluru
  var salon = {lat: -0.103971, lng: 34.752286};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 16, center: salon});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: salon, map: map});
}
</script>

  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC2wqe1uDfotYB_e-YIq8anlmLIxcy3Yhs&callback=initMap"
    async defer></script>
      <script type="text/addjavascript"
     src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js">
    </script> 
    <script type="text/javascript"
     src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/js/bootstrap.min.js">
    </script>
    <script type="text/javascript"
     src="http://tarruda.github.com/bootstrap-datetimepicker/assets/js/bootstrap-datetimepicker.min.js">
    </script>
    <script type="text/javascript"
     src="http://tarruda.github.com/bootstrap-datetimepicker/assets/js/bootstrap-datetimepicker.pt-BR.js">
    </script>
    <script type="text/javascript">
      $('#datetimepicker').datetimepicker({
        format: 'dd/MM/yyyy hh:mm:ss',
        language: 'en'
      });
    </script>


 
</body>
  <footer>
    
    
  </footer>
</html>