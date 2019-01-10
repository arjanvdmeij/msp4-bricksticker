from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    categories = Product.objects.values('category').order_by('category').distinct()
    return render(request, 'products.html', {'products':products,
        'categories':categories,
    })

    


