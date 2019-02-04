from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# Create your views here.
def search(request):
    products = Product.objects.filter(
        Q(description__icontains=request.GET['q']) | 
        Q(category__icontains=request.GET['q'])
        )
    categories = Product.objects.values(
        'category').order_by('category').distinct()
    return render(request, 'products.html', 
        {'products':products,
        'categories':categories,
    })

def filter_products(request):
    products = Product.objects.filter(
        Q(category__startswith=request.GET['q'])
        )
    categories = Product.objects.values(
        'category').order_by('category').distinct()
    return render(request, 'products.html', 
        {'products':products,
        'categories':categories,
    })