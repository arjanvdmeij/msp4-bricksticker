from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Q
from .models import Product, ProductComment
from .forms import ProductCommentForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date


def all_products(request):
    """
    View rendering all products and categories based on
    available categories named in the products
    """
    products = Product.objects.all().order_by('setnumber')
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
    View used to show a welcome page with 6 most recently added items.
    Categroies are added in for future use, though
    currently the category filter is not present
    """
    products = Product.objects.all().order_by('-date_added')[:6]
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
    
@login_required
def add_product(request):
    """
    A view for staff to add new 
    products to the database
    """
    if request.user.is_staff:
        if request.method == 'POST':
            try:
                product_form = ProductForm(request.POST, request.FILES)
                if product_form.is_valid():
                    name = product_form.cleaned_data['name']
                    setnumber = product_form.cleaned_data['setnumber']
                    
                    product_form.save()
                    
                messages.success(request, 
                    'The following product has been added:<br>' 
                    + str(setnumber) + ' - ' + name,
                    extra_tags='safe',
                    )
                return redirect(reverse('add_product'))
            except:
                messages.error(request,
                    'Someting went wrong. Please try again')
                return redirect(reverse('add_product'))
        else:
            product_form = ProductForm()
            total_users = User.objects.exclude(
                is_staff=True).all().count()
            return render(request, 'add_product.html', {
                'product_form': product_form,
                'total_users': total_users,
                })
    else:
        messages.error(request,
            'You are not allowed to use that page.')
        return redirect(reverse('index'))
