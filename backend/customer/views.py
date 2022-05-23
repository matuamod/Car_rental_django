from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Customer
from owner.models import Owner
from car.models import Car
import time

isLogin = False
isLogout = False


def index_user(request):
    global isLogin
    global isLogout

    car = Car.objects.all()
    
    return render(request,'index_user.html',{'car':car}) # I need to add migrations for car and work with index_user.html


def home(request):
    return render(request, 'home.html')


def sign_in(request):
    return render(request, 'sign_in.html')


def registration(request):
    return render(request, 'register.html')


def registrated_customer(request):
    global isLogin
    global isLogout

    customer_fname = request.POST.get('customer_fname')
    customer_lname = request.POST.get('customer_lname')    
    customer_db = request.POST.get('customer_db')
    customer_gender = request.POST.get('customer_gender')
    customer_address = request.POST.get('customer_address')
    customer_email = request.POST.get('customer_email')
    customer_password = request.POST.get('customer_password')
    customer_number = request.POST.get('customer_number')
    customer_city = request.POST.get('customer_city')
    customer_license = request.FILES['customer_license']

    check_customer = Customer.objects.filter(customer_email=customer_email)

    if not check_customer.exists():

        res_customer = Customer(
            customer_fname=customer_fname, customer_lname=customer_lname,
            customer_db=customer_db, customer_gender=customer_gender,
            customer_address=customer_address, customer_email=customer_email,
            customer_password=customer_password, customer_number=customer_number,
            customer_city=customer_city, customer_license=customer_license
        )

        res_customer.save()
        isLogin = True
        isLogout = False
        request.session['customer_email'] = customer_email
        return redirect('/home/')
    else:
        messages = 'User with such account is situated...'
        time.sleep(1)
        return render(request,'register.html',{'messages':messages})


def logined_customer(request):
    global isLogin
    global isLogout

    customer_email = request.POST.get('customer_email')
    customer__password = request.POST.get('customer_password')

    check_customer = Customer.objects.filter(customer_email=customer_email)

    if not check_customer.exists():
        messages = 'User with such account is not situated...'
        time.sleep(1)
        return render(request,'register.html',{'messages':messages})
    else:
        isLogin = True
        isLogout = False
        return redirect('/home/')


def logout_customer(request):
    global isLogin
    global isLogout

    isLogin = False
    isLogout = True
    del request.session['customer_email']
    return redirect('/')


def customer_profile(request):
    print('Hello Matua')
    if 'customer_email' in request.session:
        customer_email = request.session.get('customer_email')
        res_customer = Customer.objects.filter(customer_email=customer_email)
        return render(request, 'customer_profile.html', {'customer':res_customer})
    else:
        return redirect('/')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found... </h1>')
