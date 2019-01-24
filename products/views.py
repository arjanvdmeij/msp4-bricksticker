from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    products = Product.objects.all()
    categories = Product.objects.values('category').order_by('category').distinct()
    return render(request, 'products.html', {'products':products,
        'categories':categories,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product':product})
    


