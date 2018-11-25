{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <link rel="apple-touch-icon" sizes="76x76" href="../assets/img/apple-icon.png">
  <link rel="icon" type="image/png" href="../assets/img/favicon.png">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <title>
    Hairways Salon Management Software | Manage your salon, customer appointments and to be ranked as one of the best salons in town
  </title>
  <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
  <!--     Fonts and icons     -->
  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Roboto+Slab:400,700|Material+Icons" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css">
  <!-- CSS Files -->
  <link href="{% static 'css/assets/css/material-dashboard.css' %}" rel="stylesheet" />
  <!-- CSS Just for demo purpose, don't include it in your project -->
<!--   <link href="../assets/demo/demo.css" rel="stylesheet" /> -->

  <style>
  .card-body .show-profile input{
    background: transparent;
    border: none;
    margin-left: 10px;
  }

  .card-body .show-profile label{
    color: gray;
    font-weight: bold;
    margin-right: 10px;
  }

  .card-body .edit-profile input{
    margin-left: 10px;
    border: none;
    border-bottom: 2px solid purple;
    padding-left: 20px;
  }

  .card-body .edit-profile label{
    color: black;
    font-weight: bold;
  }

</style>

</head>


<body class="light-edition">
  <div class="wrapper ">
    <div class="sidebar" data-color="purple" data-background-color="black" data-image="{% static 'css/assets/img/sidebar-2.jpg' %}">
      <!--
        Tip 1: You can change the color of the sidebar using: data-color="purple | azure | green | orange | danger"

        Tip 2: you can also add an image using data-image tag
    -->
 <div class="logo">
        <a href="index.html" class="simple-text logo-normal">
          Hairways
        </a>
      </div>
      <div class="sidebar-wrapper">
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link" href="/dashboard/">
              <i class="material-icons">dashboard</i>
              <p>Dashboard</p>
            </a>
          </li>
          <li class="nav-item ">
            <a class="nav-link" href="/user/">
              <i class="material-icons">person</i>
              <p>User Profile</p>
            </a>
          </li>
          <li class="nav-item ">
             <a class="nav-link" href="/productsServices/">
              <i class="material-icons">content_paste</i>
              <p>Products & Services</p>
            </a>
          </li>
          <li class="nav-item ">
             <a class="nav-link" href="/staffClients/">
              <i class="material-icons">library_books</i>
              <p>Staff & Clients</p>
            </a>
          </li>
          <li class="nav-item ">
            <a class="nav-link" href="/map/">
              <i class="material-icons">location_ons</i>
              <p>Map your Salon</p>
            </a>
          </li>
          <li class="nav-item ">
            <a class="nav-link" href="/calendar/">
              <i class="material-icons">notifications</i>
              <p>Calendar</p>
            </a>

          <li class="nav-item active-pro ">
                <a class="nav-link" href="/upgrade/">
                    <i class="material-icons">unarchive</i>
                    <p>Premium Services</p>
                </a>
            </li>
        </ul>
      </div>
    </div>
    <div class="main-panel">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " id="navigation-example">
        <div class="container-fluid">
          <div class="navbar-wrapper">
            <a class="navbar-brand" href="javascript:void(0)">User Profile</a>
          </div>
          <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation" data-target="#navigation-example">
            <span class="sr-only">Toggle navigation</span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end">

            <ul class="navbar-nav">


              <li class="nav-item">
                <a class="nav-link" href="dashboard.php">
                  <i class="material-icons">dashboard</i>
                  <p class="d-lg-none d-md-block">
                    Stats
                  </p>
                </a>

              <li class="nav-item dropdown">
                <a class="nav-link" href="javscript:void(0)" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="material-icons">person</i>
                  <p class="d-lg-none d-md-block">
                    Account
                  </p>
                </a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">
                  <a class="dropdown-item" href="user.php">User profile</a>
                  <a class="dropdown-item" href="../index.html">Log out</a>

                </div>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="content">
        <div class="container-fluid">

          <div class="row">
            <div class="col-md-12">
              <div class="card">
                <div class="card-header card-header-primary">
                  <h4 class="card-title">Profile</h4>
                  <p class="card-category">Profile your salon</p>
                </div>

                <div class="card-body">
                  <button style="float: right;" name="editprofile" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-lg" class="btn btn-round btn-fill btn-info">Edit Profile</button></td>

                           <div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
                              <div class="modal-dialog modal-lg" role="document">
                                <div class="modal-content">
                                  <div class="modal-header">
                                  <div class="modal-body">

                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">&times;</span>
                                    </button>
                                    <div class="container">
                                      <div class="edit-profile">
                                        <form method="POST" action="user.php">
                                <p>
                                  <label>First name:</label>
                                  <input id="firstname" type="text" name="firstname" required>
                                </p>
                                <p>
                                  <label>Last name:</label>
                                  <input id="firstname" type="text" name="lastname" required>
                                </p>
                                <p>
                                  <label>Username:</label>
                                  <input id="firstname" type="text" name="username" required>
                                </p>
                                <p>
                                  <label>Email:</label>
                                  <input id="firstname" type="text" name="email" required>
                                </p>
                                <p>
                                  <label>Salon Name:</label>
                                  <input id="firstname" type="text" name="salonName" required>
                                </p>
                                <p>
                                  <label>Salon Description:</label>
                                  <input id="firstname" type="text" name="salonDescription" required>
                                </p>
                                <p>
                                  <label>Salon Location:</label>
                                  <input id="firstname" type="text" name="salonLocation" required>
                                </p>
                                <p>
                                  <label>Phone No:</label>
                                  <input id="firstname" type="text" name="phoneNo" required>
                                </p>
                                <p>
                                  <label>Password:</label>
                                  <input id="firstname" type="password" name="password" required>
                                </p>
                                <p>
                                  <label>Confirm Password:</label>
                                  <input id="firstname" type="password" name="confirmpass" required>
                                </p>

                                <input style="float: right;" type="submit" value="Update" name="updateprofile" class="btn btn-primary">
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                  </div>
                   <div class="show-profile">
                <p>
                  <label>First name:</label>
                  <i><b><?php echo $fname; ?></b></i>
                </p>
                <p>
                  <label>Last name:</label>
                  <i><b><?php echo $lname; ?></b></i>
                </p>
                <p>
                  <label>Username:</label>
                  <i><b><?php echo $username; ?></b></i>
                </p>
                <p>
                  <label>email:</label>
                  <i><b><?php echo $email; ?></b></i>
                </p>
                <p>
                  <label>Salon Name:</label>
                  <i><b><?php echo $salonName; ?></b></i>
                </p>
                <p>
                  <label>Salon Description:</label>
                  <i><b><?php echo $salonDescription; ?></b></i>
                </p>
                <p>
                  <label>Salon Location:</label>
                  <i><b><?php echo $salonLocation; ?></b></i>
                </p>
                <p>
                  <label>Phone No:</label>
                  <i><b><?php echo $phoneNo; ?></b></i>
                </p>
                <p>
                  <label>Password:</label>
                  <i><b>**************</b></i>
                </p>
                </div>

                </div>
              </div>
            </div>

          </div>
        </div>
      </div>

           <footer class="footer" style="color: #000">
        <div class="container-fluid">
          <nav class="float-left">
            <ul>
              <li>
                <a href="home.html">
                  Home
                </a>
              </li>
              <li>
                <a href="#">
                  About Us
                </a>
              </li>
              <li>
                <a href="#">
                  Blog
                </a>
              </li>
            </ul>
          </nav>
          <div class="copyright float-right" id="date">
        </div>
      </footer>

      <script>
        const x = new Date().getFullYear();
        let date = document.getElementById('date');
        date.innerHTML = '&copy; ' + x + date.innerHTML;
      </script>
    </div>
  </div>
  <div class="fixed-plugin">
    <div class="dropdown show-dropdown">
      <a href="#" data-toggle="dropdown">
        <i class="fa fa-cog fa-2x"> </i>
      </a>
      <ul class="dropdown-menu">
        <li class="header-title"> Sidebar Filters</li>
        <li class="adjustments-line">
          <a href="javascript:void(0)" class="switch-trigger active-color">
            <div class="badge-colors ml-auto mr-auto">
              <span class="badge filter badge-purple active" data-color="purple"></span>
              <span class="badge filter badge-azure" data-color="azure"></span>
              <span class="badge filter badge-green" data-color="green"></span>
              <span class="badge filter badge-warning" data-color="orange"></span>
              <span class="badge filter badge-danger" data-color="danger"></span>
            </div>
            <div class="clearfix"></div>
          </a>
        </li>
        <li class="header-title">Images</li>
        <li>
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-1.jpg' %}" alt="">
          </a>
        </li>
        <li class="active">
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-2.jpg' %}" alt="">
          </a>
        </li>
        <li>
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-3.jpg' %}" alt="">
          </a>
        </li>
        <li>
          <a class="img-holder switch-trigger" href="javascript:void(0)">
            <img src="{% static 'css/assets/img/sidebar-4.jpg' %}" alt="">
          </a>
        </li>

      </ul>
    </div>
  </div>

 <!--   Core JS Files   -->
 <script src="{% static 'css/assets/js/core/jquery.min.js' %}"></script>
 <script src="{% static 'css/assets/js/core/popper.min.js' %}"></script>
 <script src="{% static 'css/assets/js/core/bootstrap-material-design.min.js' %}"></script>
 <script src="https://unpkg.com/default-passive-events"></script>
 <script src="{% static 'css/assets/js/plugins/perfect-scrollbar.jquery.min.js' %}"></script>
 <!-- Place this tag in your head or just before your close body tag. -->
 <script async defer src="https://buttons.github.io/buttons.js"></script>
 <!--  Google Maps Plugin    -->
 <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY_HERE"></script>
 <!-- Chartist JS -->
 <script src="{% static 'css/assets/js/plugins/chartist.min.js' %}"></script>
 <!--  Notifications Plugin    -->
 <script src="{% static 'css/assets/js/plugins/bootstrap-notify.js' %}"></script>
 <!-- Control Center for Material Dashboard: parallax effects, scripts for the example pages etc -->
 <script src="{% static 'css/assets/js/material-dashboard.js' %}"></script>
 <!-- Material Dashboard DEMO methods, don't include it in your project! -->
 <script src="{% static 'css/assets/demo/demo.js' %}"></script>


  <!-- Change profile pic -->

  <script>
    $('#profilepic').change(function(){
      var data = new FormData();
      data.append('file', $('profilepic')[0].files[0]);
      $.ajax({
        url: 'user.php',
        type: 'POST',
        data: data,
        processData: false,
        contentType: false,
        beforeSend: function(){
          $('#profilepicView').html('Loading...');
        },
        success: function(data){
          $('#profilepic').html(<img src="'+data+'"alt="profile pic" />);
        }
        });
      return false;
      });


  </script>
  <script>
      function changeprofilepic(){
        var image = document.getElementById('profile-pic');
        var src = document.getElementById('')
        image.src="{% static 'css/assets/img/faces/avatar.jpg' %}"
      }
  </script>
  <script>
    $(document).ready(function() {
      $().ready(function() {
        $sidebar = $('.sidebar');

        $sidebar_img_container = $sidebar.find('.sidebar-background');

        $full_page = $('.full-page');

        $sidebar_responsive = $('body > .navbar-collapse');

        window_width = $(window).width();

        $('.fixed-plugin a').click(function(event) {
          // Alex if we click on switch, stop propagation of the event, so the dropdown will not be hide, otherwise we set the  section active
          if ($(this).hasClass('switch-trigger')) {
            if (event.stopPropagation) {
              event.stopPropagation();
            } else if (window.event) {
              window.event.cancelBubble = true;
            }
          }
        });

        $('.fixed-plugin .active-color span').click(function() {
          $full_page_background = $('.full-page-background');

          $(this).siblings().removeClass('active');
          $(this).addClass('active');

          var new_color = $(this).data('color');

          if ($sidebar.length != 0) {
            $sidebar.attr('data-color', new_color);
          }

          if ($full_page.length != 0) {
            $full_page.attr('filter-color', new_color);
          }

          if ($sidebar_responsive.length != 0) {
            $sidebar_responsive.attr('data-color', new_color);
          }
        });

        $('.fixed-plugin .background-color .badge').click(function() {
          $(this).siblings().removeClass('active');
          $(this).addClass('active');

          var new_color = $(this).data('background-color');

          if ($sidebar.length != 0) {
            $sidebar.attr('data-background-color', new_color);
          }
        });

        $('.fixed-plugin .img-holder').click(function() {
          $full_page_background = $('.full-page-background');

          $(this).parent('li').siblings().removeClass('active');
          $(this).parent('li').addClass('active');


          var new_image = $(this).find("img").attr('src');

          if ($sidebar_img_container.length != 0 && $('.switch-sidebar-image input:checked').length != 0) {
            $sidebar_img_container.fadeOut('fast', function() {
              $sidebar_img_container.css('background-image', 'url("' + new_image + '")');
              $sidebar_img_container.fadeIn('fast');
            });
          }

          if ($full_page_background.length != 0 && $('.switch-sidebar-image input:checked').length != 0) {
            var new_image_full_page = $('.fixed-plugin li.active .img-holder').find('img').data('src');

            $full_page_background.fadeOut('fast', function() {
              $full_page_background.css('background-image', 'url("' + new_image_full_page + '")');
              $full_page_background.fadeIn('fast');
            });
          }

          if ($('.switch-sidebar-image input:checked').length == 0) {
            var new_image = $('.fixed-plugin li.active .img-holder').find("img").attr('src');
            var new_image_full_page = $('.fixed-plugin li.active .img-holder').find('img').data('src');

            $sidebar_img_container.css('background-image', 'url("' + new_image + '")');
            $full_page_background.css('background-image', 'url("' + new_image_full_page + '")');
          }

          if ($sidebar_responsive.length != 0) {
            $sidebar_responsive.css('background-image', 'url("' + new_image + '")');
          }
        });

        $('.switch-sidebar-image input').change(function() {
          $full_page_background = $('.full-page-background');

          $input = $(this);

          if ($input.is(':checked')) {
            if ($sidebar_img_container.length != 0) {
              $sidebar_img_container.fadeIn('fast');
              $sidebar.attr('data-image', '#');
            }

            if ($full_page_background.length != 0) {
              $full_page_background.fadeIn('fast');
              $full_page.attr('data-image', '#');
            }

            background_image = true;
          } else {
            if ($sidebar_img_container.length != 0) {
              $sidebar.removeAttr('data-image');
              $sidebar_img_container.fadeOut('fast');
            }

            if ($full_page_background.length != 0) {
              $full_page.removeAttr('data-image', '#');
              $full_page_background.fadeOut('fast');
            }

            background_image = false;
          }
        });

        $('.switch-sidebar-mini input').change(function() {
          $body = $('body');

          $input = $(this);

          if (md.misc.sidebar_mini_active == true) {
            $('body').removeClass('sidebar-mini');
            md.misc.sidebar_mini_active = false;

            $('.sidebar .sidebar-wrapper, .main-panel').perfectScrollbar();

          } else {

            $('.sidebar .sidebar-wrapper, .main-panel').perfectScrollbar('destroy');

            setTimeout(function() {
              $('body').addClass('sidebar-mini');

              md.misc.sidebar_mini_active = true;
            }, 300);
          }

          // we simulate the window Resize so the charts will get updated in realtime.
          var simulateWindowResize = setInterval(function() {
            window.dispatchEvent(new Event('resize'));
          }, 180);

          // we stop the simulation of Window Resize after the animations are completed
          setTimeout(function() {
            clearInterval(simulateWindowResize);
          }, 1000);

        });
      });
    });
  </script>
</body>

</html>
