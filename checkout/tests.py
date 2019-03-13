from django.test import TestCase
from .forms import OrderForm, PaymentForm
from datetime import datetime, timedelta

class CheckoutFormTests(TestCase):
    print('Running Checkout tests')
    def test_orderform_isvalid_true(self):
        """
        check form with all required fields filled
        """
        form = OrderForm({
            'full_name':'Clint Barton',
            'address1':'Secluded 12',
            'address2':'',
            'postcode':'',
            'town_or_city':'Farawayville',
            'state_or_province':'',
            'country':'United States',
            'phone_number':'555-12345',
            'email_address':'clint@avengers.hq',
        })
        self.assertTrue(form.is_valid())

    
    def test_paymentform_isvalid_true(self):
        """
        make a variable end year (two years from now),
        for perpetual validity
        check form with all fields filled
        """
        _end_year = int(
            (datetime.now() + timedelta(weeks=104)
            ).strftime("%Y"))
            
        form = PaymentForm({
            'credit_card_number':'424242424242',
            'cvv':'111',
            'expiry_month':'11',
            'expiry_year':_end_year,
            'stripe_id':'sk_test_loadofcharacters'
        })
        self.assertTrue(form.is_valid())


    def test_orderform_isvalid_false(self):
        """
        check form with missing required field
        """
        form = OrderForm({
            'full_name':'Clint Barton',
            'address1':'Secluded 12',
            'address2':'',
            'postcode':'',
            'town_or_city':'Farawayville',
            'state_or_province':'',
            'country':'United States',
            'phone_number':'555-12345',
            'email_address':'',
        })
        self.assertFalse(form.is_valid())

    
    def test_paymentform_isvalid_false(self):
        """
        make a variable end year (two years from now),
        for perpetual validity
        check form with all fields filled
        """
        _end_year = int(
            (datetime.now() + timedelta(weeks=104)
            ).strftime("%Y"))
            
        form = PaymentForm({
            'credit_card_number':'',
            'cvv':'111',
            'expiry_month':'11',
            'expiry_year':_end_year,
            'stripe_id':'sk_test_loadofcharacters'
        })
        self.assertFalse(form.is_valid())
    
    
    def test_orderform_isvalid_false_email(self):
        """
        check form with all required fields filled
        but with an invalid email-address
        """
        form = OrderForm({
            'full_name':'Clint Barton',
            'address1':'Secluded 12',
            'address2':'',
            'postcode':'',
            'town_or_city':'Farawayville',
            'state_or_province':'',
            'country':'United States',
            'phone_number':'555-12345',
            'email_address':'clint#avengers.hq',
        })
        self.assertFalse(form.is_valid())
