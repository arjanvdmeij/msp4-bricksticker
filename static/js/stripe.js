/* global $ */

$(function() {
    $("#payment-form").submit(function() {
      var form = this;
      var card = {
        number:   $("#id_credit_card_number").val(),
        expMonth: $("#id_expiry_month").val(),
        expYear:  $("#id_expiry_year").val(),
        cvc:      $("#id_cvv").val()
      };

    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
          $("#credit-card-errors").hide();
          $("#id_stripe_id").val(response.id);
          
          // Prevent the Credit Card Details from being submitted to our server.
          // ** Modification made to require all fields in form.
          // ** Fields will be returned to server, but cleared of user data
          $("#id_credit_card_number").val('****************');
          $("#id_cvv").val('******');
          // modify entered values for expiration to accepted near-max values
          $("#id_expiry_month").css('color','white').val(12);
          $("#id_expiry_year").css('color','white').val(2035);
        
          form.submit();
        } else {
          $("#stripe-error-message").text(response.error.message);
          $("#credit-card-errors").show();
          $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
  });
});