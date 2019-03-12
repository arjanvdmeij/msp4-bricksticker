from django import forms
from .models import Product, ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment

        fields = (
            'author',
            'content',
        )
        
        widgets = {
            'content':forms.Textarea(attrs={'data-length':1000})
        }
        
class ProductForm(forms.ModelForm):
    """
    Standard form with modified label names
    """
    class Meta:
        model = Product
        
        labels = {
            'name':'Set Name',
            'setnumber':'Set Number',
            'release_year':'Set Year',
            'image1':'Select',
            'image2':"Select",
            }
        
        fields = (
            'name', 
            'setnumber', 
            'release_year', 
            'description', 
            'price', 
            'category',
            'image1', 
            'image2', 
            )
