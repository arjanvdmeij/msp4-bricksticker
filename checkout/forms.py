from django import forms
from .models import Order
from datetime import datetime, timedelta

class PaymentForm(forms.Form):
    """
    Form to obtain payment information for credit card.
    Expiration motnh and year based on 'now'
    """
    _this_year = int(
        datetime.now().strftime("%Y")
        )
    _end_year = int(
        (datetime.now() + timedelta(weeks=1040)
        ).strftime("%Y"))
    
    credit_card_number = forms.CharField(
        label='Card Nr.',
        required=False,
        )
    cvv = forms.CharField(
        label='CVV', 
        required=False,
        )
    expiry_month = forms.DecimalField(
        label='Month', 
        required=False,
        initial=1,
        min_value=1,
        max_value=12,
        )
    expiry_year = forms.DecimalField(
        label='Year', 
        required=False,
        initial=2020,
        min_value=_this_year,
        max_value=_end_year,
        )
    stripe_id = forms.CharField(
        widget=forms.HiddenInput,
        )

    
class OrderForm(forms.ModelForm):
    """
    Standard form with modified label names
    """
    class Meta:
        model = Order
        
        labels = {
            'full_name':'Full Name',
            'address1':'Address Line 1',
            'address2':'Address Line 2',
            'town_or_city':'City',
            'state_or_province':'State',
            'phone_number':"Phone #",
            'email_address':'Email'
            }
        
        fields = (
            'full_name', 
            'address1', 
            'address2', 
            'postcode', 
            'town_or_city', 
            'state_or_province', 
            'country', 
            'phone_number',
            'email_address',
            )