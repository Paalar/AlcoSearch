$(document).ready(function() {

  $(window).scroll(function(e){
    var $el = $('#buttonRow');
    var isPositionFixed = ($el.css('position') == 'fixed');
    if ($(this).scrollTop() > 200 && !isPositionFixed){
      $('#buttonRow').css({'position': 'fixed', 'top': '0px'});
    }
    if ($(this).scrollTop() < 200 && isPositionFixed)
    {
      $('#buttonRow').css({'position': 'static', 'top': '0px'});
    }
  });

$("button").click(function(){
  $("div.alkoholtype").hide();
  var classN = this.className;
  var str = classN.split(" ");
  //$("div."+str).toggle();
  if ($("div."+str).is(":visible")) {
    $("div."+str).hide();
  } else {
    $("div."+str).show();
  }
  });
});
