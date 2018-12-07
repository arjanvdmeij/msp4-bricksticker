from django.shortcuts import render

def index(request):
    """ Basically jsut an empty index page """
    return render(request, 'index.html')
