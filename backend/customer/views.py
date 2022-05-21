from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Customer
from owner.models import Owner

isLogin = False
isLogout = False


def index_user(request):
    global isLogin
    global isLogout

    if('user_email' in request.session):
        user_email = request.session.get('user_email')

        res_customer = Customer.objects.filter(customer_email=user_email)
        res_owner = Owner.objects.filter(owner_email=user_email)

        if res_customer.exists():
            request.session['user_email'] = user_email
            isLogin = True
            return redirect('/customer/')
        elif res_owner.exists():
            request.session['user_email'] = user_email
            isLogin = True
            return redirect('/owner/')


def sign_in(request):
    return render(request, 'SignIn.html')


def registration(request):
    return render(request, 'register.html')


def log_out(request):
    global isLogin
    global isLogout
    del request.session['user_email']
    isLogin = False
    isLogout = True
    Message = 'Customer logged out.'


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found... </h1>')
