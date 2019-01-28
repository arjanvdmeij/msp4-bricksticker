from django import forms
from .models import Order
from datetime import datetime, timedelta

class PaymentForm(forms.Form):
    
    _this_year = int(datetime.now().strftime("%Y"))
    _end_year = int((datetime.now() + timedelta(weeks=1040)).strftime("%Y"))
    
    MONTH_CHOICES = [(i,i) for i in range(1,13)]
    YEAR_CHOICES = [(i,i) for i in range(_this_year, _end_year)]
    
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='CVV Code', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = (
        'full_name', 
        'address1', 
        'address2', 
        'postcode', 
        'town_or_city', 
        'state_or_province', 
        'country', 
        'phone_number',
        'email_address',)