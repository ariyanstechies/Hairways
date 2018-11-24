document.querySelector('.table-striped').onclick = function(ev) {
  var checkBox = document.getElementById("check");
  var index = ev.target.parentElement.rowIndex;
  // Get the output text
  var text = document.querySelector("tr:nth-child("+index+") > td:nth-child(2)").innerHTML

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    console.log(text);
  } else {
    document.getElementById("text").innerHTML += "block";
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

$(document).ready(function(){
  $('#booked').click(function() {
    $date = $("#datetimepicker").find("input").val();

  });
});

function getTime(){
  var date = document.getElementById('Time').value;
  document.getElementById('Time').innerHTML = date;
}
<!--  Google Maps Plugin    -->
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
  $('#datetimepicker').datetimepicker({
    format: 'dd/MM/yyyy hh:mm:ss',
    language: 'en'
  });
