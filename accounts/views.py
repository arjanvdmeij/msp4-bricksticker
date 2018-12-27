from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm, UserDataForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import UserData


# Create your views here.
# def index(request):
#     """A view that displays the index page"""
#     return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    if request.user.is_superuser:
        return render(request, 'index.html')
    userdata = get_object_or_404(UserData, user_id=request.user.id)
    
    
    return render(request, 'profile.html',{
        'userdata':userdata,
    })


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        user_data_form = UserDataForm(request.POST)
        if user_form.is_valid() and user_data_form.is_valid():
            user_form.save()
            
            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                user_data = user_data_form.save(commit=False)
                user_data.user = request.user
                user_data.save()
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()
        user_data_form = UserDataForm()
    args = {
        'user_form': user_form,
        'user_data_form': user_data_form,
    }
    return render(request, 'register.html', args)

