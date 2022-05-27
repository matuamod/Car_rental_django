from audioop import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from owner.models import Owner
from car.models import Car
import time
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView 
from .forms import *
from django.urls import reverse_lazy


isLogin = False
isLogout = False


class IndexUser(ListView):
    model = Car 
    template_name = 'index_user.html'
    context_object_name = 'cars'    



site_menu = ['Main window', 'About site', 'Enter']


def about_site(request):
    return render(request, 'about_site.html', {'site_menu': site_menu, 'title': 'About site'})


class Home(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars' 
    

# def sign_in(request):
#    return render(request, 'sign_in.html') 


# def show_car(request, post_slug):

#     car = get_object_or_404(Car, slug=post_slug)

#     context = {
#         'car': car,
#         'car_brand': car.car_brand,
#         'car_model': car.car_model,
#         'car_selected': car.pk,
#     }
    
#     if 'customer_email' in request.session:
#         return render(request, 'show_car_not_login.html', context=context)
#     else:
#         return render(request, 'show_car_not_login.html', context=context)


class ShowCar(DetailView):
    model = Car
    template_name = 'show_car_not_login.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'car'


class SignIn(FormView):
    global isLogin

    form_class = CustomerLoginForm
    template_name = 'sign_in.html'
    success_message = 'Hello! You successfully log in!'
    success_url = reverse_lazy('Home')

    isLogin = True



class Registration(CreateView):
    global isLogin

    form_class = CustomerRegistrationForm
    template_name = 'register.html'
    success_message = 'Hello! You successfully made registration'
    success_url = reverse_lazy('Home')

    isLogin =True


# def registrated_customer(request):
#     global isLogin
#     global isLogout

#     customer_fname = request.POST.get('customer_fname')
#     customer_lname = request.POST.get('customer_lname')    
#     customer_db = request.POST.get('customer_db')
#     customer_gender = request.POST.get('customer_gender')
#     customer_address = request.POST.get('customer_address')
#     customer_email = request.POST.get('customer_email')
#     customer_password = request.POST.get('customer_password')
#     customer_number = request.POST.get('customer_number')
#     customer_city = request.POST.get('customer_city')
#     customer_license = request.FILES['customer_license']

#     check_customer = Customer.objects.filter(customer_email=customer_email)

#     if not check_customer.exists():

#         res_customer = Customer(
#             customer_fname=customer_fname, customer_lname=customer_lname,
#             customer_db=customer_db, customer_gender=customer_gender,
#             customer_address=customer_address, customer_email=customer_email,
#             customer_password=customer_password, customer_number=customer_number,
#             customer_city=customer_city, customer_license=customer_license
#         )

#         res_customer.save()
#         isLogin = True
#         isLogout = False
#         request.session['customer_email'] = customer_email
#         return redirect('/home/')
#     else:
#         messages = 'User with such account is situated...'
#         time.sleep(1)
#         return render(request,'register.html',{'messages':messages})


# def logined_customer(request):
#     global isLogin
#     global isLogout

#     customer_email = request.POST.get('customer_email')
#     customer__password = request.POST.get('customer_password')

#     check_customer = Customer.objects.filter(customer_email=customer_email)

#     if not check_customer.exists():
#         messages = 'User with such account is not situated...'
#         time.sleep(1)
#         return render(request,'register.html',{'messages':messages})
#     else:
#         isLogin = True
#         isLogout = False
#         return redirect('/home/')


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
