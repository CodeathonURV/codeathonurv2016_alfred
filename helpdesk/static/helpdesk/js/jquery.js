
function put_rating(p1, p2){
  $.get('/helpdesk/vote/', {comment_id: p1, rating: p2})
}
$(document).ready(function() {

   $( "#reply_button").click(function() {

       if($('#reply_container').css('display') == 'none') {
           $('#reply_container').show('fast');
       } else {
           $('#reply_container').hide('fast');
       }
   });

});
