from django.shortcuts import render
from .models import FAQ


def about(request):
    """ View showing About Stickers """
    faq = FAQ.objects.all()
    return render(request, 
        'about.html', {'faq':faq})


def privacy(request):
    """ View showing Privacy statement """
    return render(request, 
        'privacy.html')

    
def terms_and_conditions(request):
    """ View showing terms and condiotions """
    return render(request, 
        'terms_and_conditions.html')

    
def returns(request):
    """ View showing returns policy """
    return render(request, 
        'returns.html')