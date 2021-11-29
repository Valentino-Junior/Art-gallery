from django.shortcuts import render


def welcome(request):
    return render (request,'home.html')


# Create your views here.
def nav(request):
    return render (request,'navbar.html' )

def base(request):
    return render (request,'base.html' )