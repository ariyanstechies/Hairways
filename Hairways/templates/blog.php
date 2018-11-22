<!DOCTYPE html>
{% load staticfiles %}
<html>
<head>
	<title>Get beauty adviice from the best salonists in town and Best beauty experts</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1"/>

	<link rel="stylesheet" type="text/css" href="{% static 'css/salon-style.css' %}">    <!-- adding css styling -->
	<link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap/css/bootstrap.css' %}">
	<link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap/css/bootstrap-grid.css' %}">
	<link rel="stylesheet" type="text/css" href="{% static 'css/fontawesome/fontawesome.css' %}">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
	<script src="{% static 'css/javascript/jquery.js' %}"></script>
	<script src="{% static 'css/bootstrap/js/bootstrap.js' %}"></script>
	<script src="{% static 'css/javascript/javascript.js' %}"></script>
	<script src="{% static 'css/javascript/scroll-horizontal.js' %}"></script>
</head>
<body>
	<section class="head">
		<nav>
			<ul>
				<li><a href="customer/">Salons</a></li>
				<li><a href="index/">Home</a></li>
				<li><a href="blog/">Beauty advice</a></li>
			</ul>
		</nav>
	</section>

	<section class="main">
		<!-- <div style="text-align: center; margin: 100px 0px 40px 0px; color: gray">
			<p><b>There are currently no blogs</b></p>
		</div> -->

		<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://EXAMPLE.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>

	</section>

	<script id="dsq-count-scr" src="//EXAMPLE.disqus.com/count.js" async></script>
</body>
</html>
