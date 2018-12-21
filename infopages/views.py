from django.shortcuts import render
from .models import FAQ


def about(request):
    """ View showing About Stickers"""
    faq = FAQ.objects.all()
    return render(request, 'about.html', {'faq':faq})


def privacy(request):
    """ View showing About Stickers"""
    return render(request, 'privacy.html')

    
def terms_and_conditions(request):
    """ View showing About Stickers"""
    return render(request, 'terms_and_conditions.html')

    
def returns(request):
    """ View showing About Stickers"""
    return render(request, 'returns.html')