from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from checkout.models import Order, OrderItem
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv


# Create your views here.

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
    """A view that displays the profile page of a logged in user
    or alternatively shows a number of items at the behest of
    site adminsitrators and staff, specifically orders"""
    orders = Order.objects.filter(processed=False)
    order_items = OrderItem.objects.all()
    total_users = User.objects.all().count()
    return render(request, 'profile.html', {
        'orders':orders,
        'order_items':order_items,
        'total_users':total_users,
    })

def toggle_processed(request,id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=id)
        print(order)
        order.processed = not order.processed
        order.save()
        print(order.processed)
    return redirect(profile)


def forgetme(request):
    """ Log user out and remove him from table """
    if request.method == 'POST':
        remove_user = request.user.id
        try:
            u = get_object_or_404(User, pk=remove_user)
            u.delete()
            messages.success(request, 'Your account has successfully been removed')
            auth.logout(request)
            return redirect(reverse('index'))
        except:
            messages.error(request, 'Something went wrong, please contact us through the site')
            return render(request, 'profile.html')
    return render(request, 'profile.html')


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            user = auth.authenticate(
                request.POST.get('email'),
                password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()
    args = {
        'user_form': user_form,
    }
    return render(request, 'register.html', args)


def get_mail_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="newsletter.csv"'
    writer = csv.writer(response)
    all_users = User.objects.all()
    for user in all_users:
        writer.writerow([user.email])
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response