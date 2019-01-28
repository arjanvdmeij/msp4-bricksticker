from django import forms
from .models import Product, ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment

        fields = (
            'author',
            'content',
        )
