$(document).ready(function ($) {

  "use strict";

  $(window).stellar({
    responsive: false,
    parallaxBackgrounds: true,
    parallaxElements: true,
    horizontalScrolling: false,
    hideDistantElements: false,
    scrollProperty: 'scroll'
  });


  // loader
  var loader = function () {
    setTimeout(function () {
      if ($('#main-loader').length > 0) {
        $('#main-loader').removeClass('show');
      }
    }, 1);
  };
  loader();

  var carousel = function () {
    $('.carousel').owlCarousel({
      loop: true,
      margin: 10,
      nav: true,
      stagePadding: 5,
      nav: false,
      navText: ['<span class="icon-chevron-left">', '<span class="icon-chevron-right">'],
      responsive: {
        0: {
          items: 1
        },
        600: {
          items: 2
        },
        1000: {
          items: 3
        }
      }
    });

    $('.loop-block-31').owlCarousel({
      loop: true,
      margin: 0,
      nav: true,
      items: 1,
      autoplay: true,
      stagePadding: 0,
      nav: true,
      navText: ['<span class="ti-arrow-left">', '<span class="ti-arrow-right">'],
      animateOut: 'fadeOut',
      animateIn: 'fadeIn',
    });
    $('.salon-details-slider').owlCarousel({
      loop: true,
      margin: 0,
      nav: true,
      autoplay: true,
      stagePadding: 0,
      nav: true,
      dots: false,
      navText: ['<i class="ti-arrow-left">', '<i class="ti-arrow-right">'],
      animateOut: 'fadeOut',
      animateIn: 'fadeIn',
      responsive: {
        0: {
          items: 1,
          dots: true,
          nav: false
        },
        600: {
          items: 2,
          dots: true,
          nav: false
        },
        1000: {
          items: 2
        }
      }
    });

  };
  carousel();

  // navigation
  var OnePageNav = function () {
    $(".smoothscroll[href^='#'], #main-nav ul li a[href^='#']").on('click', function (e) {
      e.preventDefault();

      var hash = this.hash,
        navToggler = $('.navbar-toggler');
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 700, 'easeInOutExpo', function () {
        window.location.hash = hash;
      });


      if (navToggler.is(':visible')) {
        navToggler.click();
      }
    });
    $('body').on('activate.bs.scrollspy', function () {
      console.log('nice');
    })
  };
  OnePageNav();
  // Salon Details Page
  const toggleReviewForm = function () {
    $(".show-review-form").click(function () {
      $(".review-form").slideToggle(300);
    })
  }
  toggleReviewForm();

});


temporary = {};
jQuery('.custom-select').children().each(function () {
  var txt = jQuery(this).attr('value');
  if (temporary[txt]) {
    jQuery(this).remove();
  } else {
    temporary[txt] = true;
  }
});
// Getting selected option from drpdown
$('#location').on('change', function () {
  var location = $(this).val();
  console.log(location)
  // console.log($('.salon-location').text());
  if (location == "All Locations") {
    console.log("All was selected")
    $(".col-sm-6").show();
  } else {
    var match_location = $(".salon-location");
    for (var i = 0; i < match_location.length; i++) {
      if (location != $(match_location[i]).html()) {
        $(".col-sm-6").eq(i).hide();
      } else {
        $(".col-sm-6").eq(i).show();
      }
    }
  }
});
var salonNames = $(".salon-name");
$(".search-input").on("keyup", function () {
  var query = $(this).val();
  checkSalon(query); // call filter method
});

function checkSalon(starts_with) {
  salon_list = []
  // Iterating through each salon
  for (var y = 0; y < salonNames.length; y++) {
    if ($.trim(starts_with).length != 0) { //if there is sth in the input start filtering
      compare_salon = $(salonNames[y]).html().toLowerCase().trim();
      // comparing user input and all salon names
      if (compare_salon.startsWith(starts_with.toLowerCase())) {
        $(".col-sm-6").eq(y).show();
        salon_list.push(compare_salon);
      } else { // if didn't much hide that salon card
        $(".col-sm-6").eq(y).hide();
      }
    } else { // if input is empty show everything
      $(".col-sm-6").eq(y).show();
    }
  }
}
(function ($) {
  "use strict";
  /*==================================================================
  [ Focus Contact2 ]*/
  $('input').each(function () {
    $(this).on('blur', function () {
      if ($(this).val().trim() != "") {
        $(this).addClass('has-val');
      } else {
        $(this).removeClass('has-val');
      }
    })
  })
  /*==================================================================
  [ Validate ]*/
  var input = $('.validate-input input');
  $('.validate-form').on('submit', function () {
    var check = true;
    for (var i = 0; i < input.length; i++) {
      if (validate(input[i]) == false) {
        showValidate(input[i]);
        check = false;
      }
    }
    return check;
  });
  $('.validate-form input').each(function () {
    $(this).focus(function () {
      hideValidate(this);
    });
  });

  function validate(input) {
    if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
      if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
        return false;
      }
    } else {
      if ($(input).val().trim() == '') {
        return false;
      }
    }
  }

  function showValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).addClass('alert-validate');
  }

  function hideValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).removeClass('alert-validate');
  }
})(jQuery);
