$(document).ready(function() {
   $(".socials").hover(function(e) {
       $(this).stop().animate({
           left: e.type === "mouseenter" ? -50 : "-150px"
       }, 200);
       $(this).stop().animate({
          left: e.type === "mouseleave" ?  -150 : "-50px"
       }, 200);
   });
});