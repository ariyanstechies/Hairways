<!DOCTYPE html>
{% load staticfiles %}
<html>
<head>
  <title>For the best Salons, Barber shop in town</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/css/bootstrap-combined.min.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" media="screen"
  href="http://tarruda.github.com/bootstrap-datetimepicker/assets/css/bootstrap-datetimepicker.min.css">
  <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap/css/bootstrap-grid.css' %}">
  <link rel="stylesheet" type="text/css" href="{% static 'css/salon-style.css' %}">
    <style>
  .form-group input{
    height: 30px;
  }

  </style>

</head>
<body>



  <section class="main">
    <div class="content">
      <div class="container-fluid" style="width: 100%">
        <a href="/">
          <button class="back btn btn-primary" style="margin: 10px 0px 20px 30px;">Back home
          </button>
        </a>
        <div class="content">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-7" style="margin-bottom: 30px;">
                <div class="card">
                  <div class="card-body" style="background-image: url({% static 'css/images/1.jpg' %}); background-size: cover; height: 400px">
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

<p>{{ salon.saloonName }}</p>

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
                        <td><input type="checkbox"  id="check" class="custom-control-input" name="haircut"></td>
                        <td>Hair cut</td>
                        <td>30</td>
                        <td>100</td>
                      </tr>
                      <tr>
                        <td><input type="checkbox"  id="check" class="custom-control-input" name="haircut"></td>
                        <td>Blow dry</td>
                        <td>45</td>
                        <td>300</td>
                      </tr>
                      <tr>
                        <td><input type="checkbox"  class="custom-control-input" name="haircut"></td>
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
                  <div id="text"></div>
                  <p id="total"></p>
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

                                <img src="{% static 'css/images/success.png' %}" style="height: 100px; width: 100px; margin: 20px 0px 0px 0px; " align="center">

                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC2wqe1uDfotYB_e-YIq8anlmLIxcy3Yhs&callback=initMap" async defer></script>
  <script src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/js/bootstrap.min.js"> </script>
  <script src="http://tarruda.github.com/bootstrap-datetimepicker/assets/js/bootstrap-datetimepicker.min.js"></script>
  <script src="http://tarruda.github.com/bootstrap-datetimepicker/assets/js/bootstrap-datetimepicker.pt-BR.js"></script>
<script type="text/javascript">
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
  <script src="{% static 'css/bootstrap/js/bootstrap.js' %}"></script>
  <script src="{% static 'css/javascript/javascript.js' %}"></script>
  <script src="{% static 'css/javascript/moreinfo.js' %}"></script>

  <script src="{% static 'css/javascript/scroll-horizontal.js' %}"></script>
</body>
<footer>
</footer>
</html>
