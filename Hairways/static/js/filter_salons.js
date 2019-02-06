$(window).on('load',function() {
  jaymoh();
});
$("#location").on('change',function() {
  alert("Hey there");
  console.log("Hey its me");
  jaymoh();
});
function jaymoh(){

    var location = $("#location").val();
    $.ajax({
      type: "GET",
      url: "/locations/",
      data: {
        'location': location
      },
      success: function (data) {
        var res=$.parseJSON(data);
        jQuery.each(res, function(index, result){
          // console.log(result.fields.location);
        $(".date").html(result.model);
        $("#salon_location").html(result.fields.location);
        $("#description h1").html(result.fields.saloonName);
        $("#description h2").html(result.fields.location);
        $(".salon_descri").html(result.fields.description);
        $(".fa .fa-eye .fa-2x").html(result.fields.views);
        $(".fa .fa-heart-o .fa-2x").html(result.fields.likes);
        // $(".fa .fa-envelope-o .fa-2x").html(result.fields.approved_comments.count);
        $(".fa .fa-share-alt .fa-2x").html(result.fields.shares);
        $(".fa .fa-heart-o .fa-2x").html(result.fields.likes);
        $("#view_mobile").html(result.fields.likes);
        });
      },
      error: function(error){
            console.log(error);
         }
    });

}
