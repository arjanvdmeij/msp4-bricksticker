/* global $ */

function showProductSlide(n) {
  var i, slideIndex = n;
  var x = document.getElementsByClassName("productSlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  $(x[i]).fadeOut(1000);
  $(x[slideIndex-1]).fadeIn(1000);
  x[slideIndex-1].style.display = "block";
}
