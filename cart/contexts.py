from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Make cart contents available when rendering any page.
    Also provide list of product IDs to use for marking
    items that were added to cart already
    """
    cart = request.session.get('cart', {})
    cart_items = []
    cart_ids = list()
    total = 0
    product_total_price = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_total_price = quantity * product.price
        product_count += quantity
        cart_items.append({
            'id':id, 
            'quantity': quantity, 
            'product': product, 
            'product_total_price': product_total_price,
            })
        cart_ids.append(int(id))
    return { 
        'cart_items': cart_items, 
        'total': total, 
        'product_count': product_count,
        'cart_ids': cart_ids,
        }