from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Q
from .models import Product, ProductComment
from .forms import ProductCommentForm
from datetime import date


def all_products(request):
    """
    View rendering all products and categories based on
    available categories named in the products
    """
    products = Product.objects.all()
    categories = Product.objects.values(
        'category').order_by(
        'category').distinct()
    return render(request, 
        'products.html', 
        {'products':products,
        'categories':categories,
    })

    
def latest_products(request):
    """
    View used to show a welcome page with 5 most recently added items.
    Categroies are added in for future use, though
    currently the category filter is not present
    """
    products = Product.objects.all().order_by('-date_added')[:5]
    categories = Product.objects.values(
        'category').order_by(
        'category').distinct()
    return render(request, 
        'index.html', 
        {'products':products,
        'categories':categories,
    })


def product_detail(request, pk):
    """
    View rendering the detailed product page for the product 
    selected from the products page, including the available
    comments on that particular product
    """
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        
        if form.is_valid:
            product = get_object_or_404(Product, pk=pk)
            ProductComment.objects.create(
                comment_on=product,
                author=form['author'].value(),
                content=form['content'].value(),
                date = date.today(),
                )
            comments = ProductComment.objects.filter(comment_on=pk).order_by('-date')
            comment_form = ProductCommentForm()
            return redirect('productdetail', product.id)
    else:
        product = get_object_or_404(Product, pk=pk)
        comments = ProductComment.objects.filter(comment_on=pk).order_by('-date')
        comment_form = ProductCommentForm()
        return render(request, "productdetail.html", {
            'comment_form':comment_form,
            'product':product,
            'comments':comments,
        })
    
