from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# Create your views here.
def search(request):
    """
    View returning the filtered results after
    submitting a search string
    """
    search = request.GET['q']
    products = Product.objects.filter(
        Q(description__icontains=request.GET['q']) | 
        Q(category__icontains=request.GET['q'])
        )
    categories = Product.objects.values(
        'category').order_by('category').distinct()
    return render(request, 'products.html', 
        {'products':products,
        'categories':categories,
        'search':search,
    })

def filter_products(request):
    """
    View returning a filtered list of products after selecting
    a category from the dropdown menu
    """
    picked = request.GET['q']
    products = Product.objects.filter(
        Q(category__startswith=request.GET['q'])
        )
    categories = Product.objects.values(
        'category').order_by('category').distinct()
    return render(request, 'products.html', 
        {'products':products,
        'categories':categories,
        'picked':picked,
    })