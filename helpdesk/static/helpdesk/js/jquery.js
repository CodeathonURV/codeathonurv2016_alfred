$(document).ready(function() {

  $('#rating').click(function(){
      console.log("hola que tal");

      var comid
      comid = $(this).attr("data-comid");
      $.get('/helpdesk/vote/', {comment_id: comid}, function(data){
                 $('#rating_value').html(data);
                 $('#rating').hide();
      });
  });


});
