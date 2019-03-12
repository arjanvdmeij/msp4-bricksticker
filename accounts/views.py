from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv


def logout(request):
    """
    A simple view that logs the user out and 
    redirects back to the index page
    """
    auth.logout(request)
    messages.success(request, 'You have successfully signed out')
    return redirect(reverse('index'))


def login(request):
    """
    A view that manages the login form
    """
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserLoginForm(request.POST)
            if user_form.is_valid():
                user = auth.authenticate(request.POST['username_or_email'],
                                         password=request.POST['password'])
    
                if user and user.is_active:
                    auth.login(request, user)
                    messages.error(request, "You have successfully signed in")
    
                    if request.GET and request.GET['next'] !='':
                        next = request.GET['next']
                        return HttpResponseRedirect(next)
                    else:
                        return redirect(reverse('index'))
                elif user and not user.is_active:
                    user_form.add_error(None,
                        "Your account is inactive."
                        + " Please contact the site owner for assistance")
                else:
                    user_form.add_error(None, 
                        "Your username and/or password are incorrect")
        else:
            user_form = UserLoginForm()
    else:
        messages.error(request,
            "You are already logged in")
        return redirect(reverse('index'))

    return render(request, 'login.html', {
        'user_form': user_form, 
        'next': request.GET.get('next', ''),
    })


@login_required
def profile(request):
    """
    Profile view with 'delete me'
    """
    return render(request, 'profile.html')


@login_required
def forgetme(request):
    """ 
    Log out and remove the user's account
    Button disabled for staff
    """
    if request.method == 'POST':
        remove_user = request.user.id
        try:
            u = get_object_or_404(User, pk=remove_user)
            u.delete()
            messages.success(request, 
                'Your account has successfully been removed')
            auth.logout(request)
            return redirect(reverse('index'))
        except:
            messages.error(request, 
                'Something went wrong, please contact us through the site')
            return render(request, 'profile.html')
    return render(request, 'profile.html')


def register(request):
    """
    A view for the registration form
    """
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                
                user = auth.authenticate(
                    request.POST.get('email'),
                    password=request.POST.get('password1'))
    
                if user:
                    auth.login(request, user)
                    messages.success(request, 
                        "You have successfully registered. Thank you!")
                    return redirect(reverse('index'))
    
                else:
                    messages.error(request, 
                        "We failed to sign you in, please try again later!")
        else:
            user_form = UserRegistrationForm()
    else:
        messages.error(request,
            "You are already logged in")
        return redirect(reverse('index'))
    
    return render(request, 'register.html', {
        'user_form': user_form,
    })

@login_required
def get_mail_csv(request):
    """ 
    Allow admins/staff to download a csv file
    for newsletter purposes
    """
    if request.user.is_staff:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="newsletter.csv"'
        writer = csv.writer(response)
        all_users = User.objects.exclude(is_staff=True).all()
        writer.writerow(['Email address', 'First Name', 'Last Name'])
        for user in all_users:
            writer.writerow([user.email, user.first_name, user.last_name])
        return response
    else:
        return render(request, 'index.html')