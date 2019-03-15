from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def view_cart(request):
    """
    Renders the cart contents page
    """
    return render(request, "cart.html")
    
    
def add_to_cart(request, id):
    """
    Add a product to the cart.
    While site doesn't offer quantity at the moment,
    option is here if wanted in future
    """
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] += quantity
    else:
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
def adjust_cart(request, id):
    """
    Adjust the quantity of a product to the specified amount
    or delete an item from the cart
    """
    if request.POST.get('quantity') == '':
        request.session['cart'] = request.session.get('cart', {})
        return redirect(reverse('view_cart'))
    else:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))