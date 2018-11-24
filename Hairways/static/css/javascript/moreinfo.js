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

  $(document).ready(function(){
    $('#booked').click(function() {
      $date = $("#datetimepicker").find("input").val();

    });
  });

  function getTime(){
    var date = document.getElementById('Time').value;
    document.getElementById('Time').innerHTML = date;
  }

  $('#datetimepicker').datetimepicker({
    format: 'dd/MM/yyyy hh:mm:ss',
    language: 'en'
  });

});
