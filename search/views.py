from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# Create your views here.
def search(request):
    products = Product.objects.filter(
        Q(description__icontains=request.GET['q']) | Q(category__icontains=request.GET['q'])
        )
    categories = Product.objects.values('category').order_by('category').distinct().filter(
        Q(description__icontains=request.GET['q']) | Q(category__icontains=request.GET['q'])
        )
    return render(request, 'products.html', {'products':products,
        'categories':categories,
        
    })