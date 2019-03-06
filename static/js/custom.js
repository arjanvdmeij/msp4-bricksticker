/* global $ */

function showProductSlide(n) {
  var i, slideIndex = n;
  var x = document.getElementsByClassName("productSlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
    x[i].style.margin = "0 auto";
  }
  $(x[i]).fadeOut(1000);
  $(x[slideIndex-1]).fadeIn(1000);
  x[slideIndex-1].style.display = "block";
  x[slideIndex-1].style.margin = "0 auto";
}

$(document).ready(function(){
  $('.slider').slider({
    indicators: false,
    duration: 2500,
    interval: 3500,
    height: 120
  });
  $('.collapsible').collapsible();
  $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
  $('select').formSelect();
  $('.btn-alert').on('click', function() {
    $('#alert-box').fadeTo(1000,0, function() {
      $('#alert-box').addClass('hide');
      });
    });
});
