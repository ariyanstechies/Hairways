$(document).ready(function(){
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
    if (index === -1){
        checkoutItems.push({item:item,cost:cost});
    }
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
});