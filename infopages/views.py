from django.shortcuts import render, reverse, redirect
from .models import FAQ
from .forms import FAQForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


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

@login_required
def add_faq(request):
    """
    A view for staff to add a new
    FAQ item to the database
    """
    if request.user.is_staff:
        if request.method == 'POST':
            try:
                faq_form = FAQForm(request.POST)
                if faq_form.is_valid():
                    faq_form.save()
                messages.success(request, 
                    'The FAQ item has been added. The question was:<br>'
                    + faq_form.cleaned_data['question'],
                    extra_tags='safe',
                    )
                return redirect(reverse('add_faq'))
            except:
                messages.error(request,
                    'Someting went wrong. Please try again')
                return redirect(reverse('add_faq'))
        else:
            faq_form = FAQForm()
            total_users = User.objects.exclude(is_staff=True).all().count()
            return render(request, 'add_faq.html', {
                'faq_form': faq_form,
                'total_users': total_users,
                })
    else:
        messages.error(request,
            'You are not allowed to use that page.')
        return redirect(reverse('index'))