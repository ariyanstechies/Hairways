<!DOCTYPE html>
<html>
<head>
	<title>For the best Salons, Barber shop in town</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1"/>

	<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
	
	<link rel="stylesheet" type="text/css" href="salon-style.css">    <!-- adding css styling -->
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap-grid.css">
	<link rel="stylesheet" type="text/css" href="fontawesome/fontawesome.css">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
	<script src="javascript/jquery.js"></script>
	<script src="bootstrap/js/bootstrap.js"></script>
	<script src="javascript/javascript.js"></script>
	<script src="javascript/scroll-horizontal.js"></script>

	<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700,800' rel='stylesheet' type='text/css'>
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript">
        $(document).ready(function() {
            $(".dropdown img.flag").addClass("flagvisibility");

            $(".dropdown dt a").click(function() {
                $(".dropdown dd ul").toggle();
            });
                        
            $(".dropdown dd ul li a").click(function() {
                var text = $(this).html();
                $(".dropdown dt a span").html(text);
                $(".dropdown dd ul").hide();
                $("#result").html("Selected value is: " + getSelectedValue("sample"));
            });
                        
            function getSelectedValue(id) {
                return $("#" + id).find("dt a span.value").html();
            }

            $(document).bind('click', function(e) {
                var $clicked = $(e.target);
                if (! $clicked.parents().hasClass("dropdown"))
                    $(".dropdown dd ul").hide();
            });


            $("#flagSwitcher").click(function() {
                $(".dropdown img.flag").toggleClass("flagvisibility");
            });
        });
     </script>
<!-- start menu -->     
<link href="css/megamenu.css" rel="stylesheet" type="text/css" media="all" />
<script type="text/javascript" src="js/megamenu.js"></script>
<script>$(document).ready(function(){$(".megamenu").megamenu();});</script>
<!-- end menu -->
<!-- top scrolling -->
<script type="text/javascript" src="javascript/move-top.js"></script>
<script type="text/javascript" src="javascript/easing.js"></script>
   <script type="text/javascript">
		jQuery(document).ready(function($) {
			$(".scroll").click(function(event){		
				event.preventDefault();
				$('html,body').animate({scrollTop:$(this.hash).offset().top},1200);
			});
		});
	</script>

	
</head>



<body id="body" onbeforeunload="HandleBackFunctionality()" style="background-color: whitesmoke">

	<!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/5baebdae8a438d2b0cdfd6d9/default';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();http://localhost/salon/customer.php#carouselExampleIndicators
</script>
<!--End of Tawk.to Script-->

	<section class="head">
		<nav>
			<ul>
				<li><a href="index.html">Home</a></li>
				<li><a href="blog.php">FAQs</a></li>
			</ul>
		</nav>
	</section>

				<!-- RANKING SALONS IN SLIDER -->
	<section class="salon-rank">
	
		<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
			<ol class="carousel-indicators">
			    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
			    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
			    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
			</ol>
			<div class="carousel-inner">
				<div class="carousel-item active">
				    <img class="d-block w-100" src="images/34.jpg" alt="First slide">
				    <div class="carousel-caption d-none d-md-block">
					    <h5 style="color: #11AFF2; font-weight: bold;">Tuskys Salon</h5>
						<p style="color: #000">For the best and latest cuts</p>
					</div>
				</div>

				<div class="carousel-item">
				    <img class="d-block w-100" src="images/cover1.jpg" alt="Second slide">
				    <div class="carousel-caption d-none d-md-block">
					    <h5 style="color: #11AFF2; font-weight: bold;">Tuskys Salon</h5>
						<p style="color: #000;">For the best and latest cuts</p>
					</div>
				</div>

			    <div class="carousel-item">
				    <img class="d-block w-100" src="images/salon.jpg" alt="Third slide">
				    <div class="carousel-caption d-none d-md-block">
					    <h5 style="color: #11AFF2; font-weight: bold;">Tuskys Salon</h5>
						<p style="color: #000;">For the best and latest cuts</p>
					</div>
				    </div>
			</div>
				
				<a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
			    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
			    <span class="sr-only">Previous</span>
			  </a>
			  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
			    <span class="carousel-control-next-icon" aria-hidden="true"></span>
			    <span class="sr-only">Next</span>
			  </a>
		</div>
	</section>

	<div class="main">
                <div class="wrap">
             	  
				  <div class="content-bottom">
				   <div class="box1">
				    <div class="col_1_of_3 span_1_of_3"><a href="moreInfo.php">
				     <div class="view view-fifth">
				  	  <div class="top_box">
					  	<h3 class="m_1">Hairways Salon</h3>
					  	<p class="m_2">Salon and Spa</p>
				         <div class="grid_img">
						   <div class="css3"><img src="images/1.jpg" alt=""/></div>
					          <div class="mask">
	                       		<div class="info">Book appointment</div>
			                  </div>
	                    </div>
                       <div class="location"><h3>Mega city</h3></div>
					   </div>
					    </div>
					   
						 
			    	    <div class="clear"></div>
			    	</a></div>
				    <div class="col_1_of_3 span_1_of_3"><a href="moreInfo.php">
				     <div class="view view-fifth">
				  	  <div class="top_box">
					  	<h3 class="m_1">Better Cutz</h3>
					  	<p class="m_2">Barber shop</p>
					    <div class="grid_img">
						   <div class="css3"><img src="images/2.jpg" alt=""/></div>
					          <div class="mask">
	                       		<div class="info">Book appoinyment</div>
			                  </div>
	                    </div>
                       <div class="location"><h3>Mega city</h3></div>
					   </div>
					    </div>
					   
						 
			    	    <div class="clear"></div>
			    	</a></div>
				    <div class="col_1_of_3 span_1_of_3"><a href="moreInfo.php">
				     <div class="view view-fifth">
				  	  <div class="top_box">
					  	<h3 class="m_1">Hair clinic</h3>
					  	<p class="m_2">Tuskys</p>
				         <div class="grid_img">
						   <div class="css3"><img src="images/3.jpg" alt=""/></div>
					          <div class="mask">
	                       		<div class="info">Book appoinment</div>
			                  </div>
	                    </div>
                       <div class="location"><h3>Mega city</h3></div>
					   </div>
					    </div>
					   
						 
			    	    <div class="clear"></div>
			    	</a></div>
				  <div class="clear"></div>
			  </div>
			  <div class="box1">
				  <div class="col_1_of_3 span_1_of_3"><a href="moreInfo.php">
				     <div class="view view-fifth">
				  	  <div class="top_box">
					  	<h3 class="m_1">Your beauty</h3>
					  	<p class="m_2">Salon and spa</p>
				         <div class="grid_img">
						   <div class="css3"><img src="images/4.jpg" alt=""/></div>
					          <div class="mask">
	                       		<div class="info">Book appointment</div>
			                  </div>
	                    </div>
                       <div class="location"><h3>Mega city</h3></div>
					   </div>
					    </div>
					   
						 
			    	    <div class="clear"></div>
			    	</a></div>
				    <div class="col_1_of_3 span_1_of_3"><a href="moreInfo.php">
				     <div class="view view-fifth">
				  	  <div class="top_box">
					  	<h3 class="m_1">Smart Barbershop</h3>
					  	<p class="m_2">Barber shop</p>
				         <div class="grid_img">
						   <div class="css3"><img src="images/5.jpg" alt=""/></div>
					          <div class="mask">
	                       		<div class="info">Book appointment</div>
			                  </div>
	                    </div>
                       <div class="location"><h3>Mega city</h3></div>
					   </div>
					    </div>
					   
						 
			    	    <div class="clear"></div>
			    	</a></div>
				   <div class="col_1_of_3 span_1_of_3"><a href="moreInfo.php">
				     <div class="view view-fifth">
				  	  <div class="top_box">
					  	<h3 class="m_1">We make salon</h3>
					  	<p class="m_2">Salon</p>
				         <div class="grid_img">
						   <div class="css3"><img src="images/6.jpg" alt=""/></div>
					          <div class="mask">
	                       		<div class="info">Book appointment</div>
			                  </div>
	                    </div>
                       <div class="location"><h3>Mega city</h3></div>
					   </div>
					    </div>
					   
						 
			    	    <div class="clear"></div>
			    	</a></div>
				  <div class="clear"></div>
			    </div>
			  </div>
			 </div>
        </div>

        <div class="footer" style="background-color: gray">
       	  
       	 
       	 <div class="footer-bottom" style="padding: 50px 0px 50px 0px">
       	 	<div class="wrap">
       	 		<div class="section group">
				<div class="col_1_of_5 span_1_of_5">
					<h3 class="m_9">Home</h3>
					
			             
				</div>
				<div class="col_1_of_5 span_1_of_5">
					<h3 class="m_9">Beauty Blog</h3>
					
				</div>
				<div class="col_1_of_5 span_1_of_5">
					<h3 class="m_9">Contact us</h3>
					
				</div>
				
				
			</div>
       	 	</div>
       	 </div>
       	
       </div>
       <script type="text/javascript">
			$(document).ready(function() {
			
				var defaults = {
		  			containerID: 'toTop', // fading element id
					containerHoverID: 'toTopHover', // fading element hover id
					scrollSpeed: 1200,
					easingType: 'linear' 
		 		};
				
				
				$().UItoTop({ easingType: 'easeOutQuart' });
				
			});
		</script>
		<a href="#" id="toTop" style="display: block;"><span id="toTopHover" style="opacity: 1;"></span></a>
        
		

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
    async defer>
  </script>


</body>
	
</html>

