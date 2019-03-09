from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ

        fields = (
            'question',
            'answer',
            )
        
        labels = {
            'question':'Enter the Question',
            'answer':'Give the Answer',
            }