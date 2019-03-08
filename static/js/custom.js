/* global $ */

// Switch betwen available images on productdetail page
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

// smooth scroll to top for all pages
$('a[href="#top"]').on('click', function(top) {
    var scrollId = $(this.hash);
    top.preventDefault();
    $('html, body').animate({
      scrollTop: scrollId.offset().top
    }, 1000, function() {
      // Callback after animation, setting focus
      var $focusOn = $(scrollId);
      $focusOn.focus();
    });
  });

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
  // custom alert-box closing
  $('.btn-alert').on('click', function() {
    $('#alert-box').fadeTo(1000,0, function() {
      $('#alert-box').addClass('hide');
      });
    });
});
