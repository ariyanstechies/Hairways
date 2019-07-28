$(document).ready(function(){
  document.querySelector('.table-striped').onclick = function(ev) {
    var index = ev.target.parentElement.rowIndex;
    var currentRow = $("tr:nth-child("+index+")");
    if (currentRow.find(".custom-control-input").is(':checked')) {
      currentRow.find(".custom-control-input").prop("checked", false);
    } else {
      currentRow.find(".custom-control-input").prop("checked", true);
    }
    var checkBox = document.querySelector("tr:nth-child("+index+") > td:nth-child(1) > input");
    var text = document.querySelector("tr:nth-child("+index+") > td:nth-child(2)").innerHTML

    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
      document.getElementById("text").innerHTML += '<div>'+ text +'</div>'+'<br>';
    } else {
      // document.getElementById("text").innerHTML -= text;
    }
  }

  function getTime(){
    var date = document.getElementById('Time').value;
    document.getElementById('Time').innerHTML = date;
  }

  $('#datetimepicker').datetimepicker({
    format: 'dd/MM/yyyy hh:mm:ss',
    language: 'en'
  });

$('.carousel-inner').find('.comments-section:first').addClass('active');

// Handling number of views
$(window).on('load', function(){
  var parent = $(this).parent();
  var salonId= {{salon.id}};
  $.ajax({
    url: '{% url "update_views" %}',
    type: 'POST',
    data: {
      'salonId': salonId,
    }});
});
// adding and removing items from cart
checkoutItems = [];
$("tr").on("click", function(e){
  $("input[type='checkbox']", this).each( function() {
    $(this).attr('checked', !$(this).attr('checked'));
  });

  var isChecked = $(this).find('input:checkbox').prop('checked');
    item=$(this).children('td').eq(1).html();
  cost=parseInt($(this).children('td').eq(2).html(),10);
  var elem = '<div class="row show_item">&plus;<div class="col-sm">'+item+'</div><div class="col-sm">'+cost+'</div></div>';
  var current = parseInt($(".SubTotal span").html(), 10);
  if(isChecked){
    $("#show_cart").append($.parseHTML(elem));
    $(".SubTotal span").html(current+=cost);

    var index = checkoutItems.findIndex(x => x.item==item)
    console.log(index)   // here you can check specific property for an object whether it exist in your array or not
    if (index === -1){
        checkoutItems.push({item:item,cost:cost});
    }
    else console.log("object already exists")

  console.log(checkoutItems)
  console.log(item)
  }
  else {
    // Iterating through each item in cart
    var cartItems = $(".show_item");
    for (var y=0; y<cartItems.length; y++){
      get_item1 = $(cartItems[y]).children('div').eq(0).html().trim();
      get_item2 = $(cartItems[y]).children('div').eq(1).html().trim();
      if (get_item1 == item && get_item2==cost) {

        $(cartItems[y]).remove(); //removing current div if match found

        // removing unchecked services from final checkout table
        var removeByAttr = function(checkoutItems, attr, value){
        var i = checkoutItems.length;
        while(i--){
           if( checkoutItems[i]
               && checkoutItems[i].hasOwnProperty(attr)
               && (arguments.length > 2 && checkoutItems[i][attr] === item ) ){
               checkoutItems.splice(i,1);
           }
        }
        return checkoutItems;
    }
        removeByAttr(checkoutItems, "item", item);
        console.log(checkoutItems)
      }
    }
    if (current !=0) {
      $(".SubTotal span").html(current-=cost)
    }
  }
});


function display() {
var checkout = checkoutItems
$('#display_checkout tbody').html('');

function addDataToTbody(nl, data) { // nl -> NodeList, data -> array with objects
  data.forEach((d, i) => {
    var tr = nl.insertRow(i);
    Object.keys(d).forEach((k, j) => { // Keys from object represent th.innerHTML
      var cell = tr.insertCell(j);
      cell.innerHTML = d[k]; // Assign object values to cells
    });
    nl.appendChild(tr);
  })
}

var lakeTbody = document.querySelector("#display_checkout tbody");

addDataToTbody(lakeTbody, checkout);
var firstDivContent = document.getElementById('SubTotal');
var secondDivContent = document.getElementById('total');
secondDivContent.innerHTML = "Total: "+firstDivContent.innerHTML;
}

$(document).ready(function(){
    $('#booked').click(function() {
      $date = $("#datetimepicker").find("input").val();

    });
  });