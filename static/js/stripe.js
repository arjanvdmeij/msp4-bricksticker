/* global $ */

/**********************************************************************************
 * Modifications were made to require all fields in form.
 * As a result, clearing the form as the original stripe.js did, breaks things.
 * Instead, Fields will now be returned to server, but cleared of user data
 * Expiration month and year are set 15+ years into the future
 * Card Number and CVV are changed to fields of asterisks
 * 
 * This is an intermediate solution until the upgrade to Stripev3 is done
 * at which point the stripe.js file becomes unnecessary
 * 
 **********************************************************************************/

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
          $("#id_credit_card_number").val('****************');
          $("#id_cvv").val('******');
          // ** modify entered values for expiration to accepted near-max values
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