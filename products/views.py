from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Q
from .models import Product, ProductComment
from .forms import ProductCommentForm
from datetime import date

def all_products(request):
    products = Product.objects.all()
    categories = Product.objects.values(
        'category').order_by(
        'category').distinct()
    return render(request, 
        'products.html', 
        {'products':products,
        'categories':categories,
    })

# def filtered_products(request, selected):
#     products = Product.objects.filter(category=selected).order_by('setnumber')
#     categories = Product.objects.all.values(
#         'category').order_by(
#         'category').distinct()
#     return render(request, 
#         'products.html', 
#         {'products':products,
#         'categories':categories,
#     })
  
    
def latest_products(request):
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
    
