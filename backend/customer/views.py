from audioop import reverse
from datetime import datetime
from datetime import date
from distutils.command.clean import clean
import http
from urllib import request
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Customer
from owner.models import Owner
from car.models import Car
import time
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from django.views.generic.edit import FormMixin, ModelFormMixin
from .forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from car_rent.models import RentCar
import logging


isLogin = False
isLogout = False
CustomerEmail = ''

logger = logging.getLogger(__name__)


class IndexUser(ListView):
    model = Car
    template_name = 'index_user.html'
    context_object_name = 'cars'
    logger.warning('Current template_name: index_user.html')
    logger.info('Default index_user_ page for user, which is not login')


site_menu = ['Main window', 'About site', 'Enter']


def about_site(request):
    logger.warning('Current template_name: about_site.html')
    logger.info('Show some information about our Car Rental site')
    return render(request, 'about_site.html', {'site_menu': site_menu, 'title': 'About site'})


class Home(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'
    logger.warning('Current template_name: home.html')
    logger.info('User is identified, so he can rent a car!')


class ShowCar(DetailView):
    model = Car
    template_name = 'show_car_not_login.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'car'
    logger.warning('Current template_name: show_car_not_login.html')
    logger.info('Only show cars for user, which is not login')


class SignIn(FormView, FormMixin):
    global isLogin
    global isLogout
    global CustomerEmail

    form_class = CustomerLoginForm
    template_name = 'sign_in.html'
    success_message = 'Hello! You successfully log in!'
    success_url = reverse_lazy('Home')
    logger.warning('Current template_name: sign_in.html')

    def form_valid(self, form):
        customer_email = form.cleaned_data.get('customer_email')
        logger.info(f'Current customer email: {customer_email}')

        customer_password = form.cleaned_data.get('customer_password')
        logger.info(f'Current customer password: {customer_password}')

        if customer_email and customer_password:
            customer = Customer.objects.filter(customer_email=customer_email,
                                               customer_password=customer_password)
            if not customer.exists():
                unsuccess_message = 'No account with such data...'
                logger.warning(unsuccess_message)
                time.sleep(1)
                logger.warning('Redirect to sign_in')
                return render(self.request, 'sign_in.html', {'messages': unsuccess_message})

            else:
                success_message = 'Successfully logged in'
                global isLogin
                global isLogout
                global CustomerEmail
                isLogin = True
                isLogout = False
                CustomerEmail = customer_email
                logger.warning(success_message)
                return super().form_valid(form)
        else:
            logger.warning('Redirect to registration')
            return redirect('registration/')


class Registration(CreateView, ModelFormMixin):
    global isLogin
    global isLogout
    global CustomerEmail

    form_class = CustomerRegistrationForm
    template_name = 'register.html'
    success_message = 'Hello! You successfully made registration'
    success_url = reverse_lazy('Home')
    logger.warning('Current template_name: register.html')

    def form_valid(self, form):
        global isLogin
        global isLogout
        isLogin = True
        isLogout = False
        logger.warning(self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        unsuccess_message = 'User with such account is situated...'
        logger.warning(unsuccess_message)
        time.sleep(1)
        logger.warning('Redirect to registration')
        return render(self.request, 'register.html', {'messages': unsuccess_message})


class LogoutCustomer(ListView):
    global isLogin
    global isLogout

    model = Car
    template_name = 'index_user.html'
    context_object_name = 'cars'
    isLogin = False
    isLogout = True
    logger.warning('Current template_name: index_user.html')
    logger.warning('Successfully logged out')


class CustomerProfile(TemplateView):
    template_name = 'customer_profile.html'
    logger.warning('Current template_name: customer_profile.html')

    def get(self, request):
        customers = Customer.objects.all()
        args = {'customers': customers}
        return render(request, self.template_name, args)


# class CheckAvailabilityNotLogin(FormView, FormMixin):
#     global isLogin
#     global isLogout

#     form_class = CheckAvailabilityForm
#     template_name = 'show_car_not_login.html'
#     success_message = 'Hello! You successfully check availability!'
#     success_url = reverse_lazy('Home')

#     def form_valid(self, form):
#         print('Hi')
#         date_of_booking = form.cleaned_data.get('date_of_booking')
#         date_of_return = form.clened_data.get('date_of_return')

#         current_customer = Customer.objects.filter(customer_id=self.kwargs['pk'])
#         print(type(current_customer))
#         current_car = Car.objects.filter(car_id=self.kwargs['pk'])

#         return redirect('/')


def CheckAvailability(request, car_id):
    global isLogin
    global CustomerEmail

    if isLogin == False:
        logger.warning('Redirect to sign_in')
        return redirect('/sign_in/')

    date_of_booking = request.POST.get('date_of_booking', '')
    date_of_return = request.POST.get('date_of_return', '')

    date_of_booking = datetime.strptime(date_of_booking, '%Y-%m-%d').date()
    date_of_return = datetime.strptime(date_of_return, '%Y-%m-%d').date()
    logger.info(f'Date of booking: {date_of_booking}')
    logger.info(f'Date of return: {date_of_return}')

    current_car = Car.objects.get(pk=car_id)
    rent_cars = RentCar.objects.filter(rent_car_plate=current_car.car_plate)

    customer_email = CustomerEmail
    customer = Customer.objects.filter(customer_email=customer_email)

    if customer.exists():
        for cust in customer:
            current_customer = cust
    else:
        unsuccess_messaage = 'You not already sign in!'
        logger.warning(unsuccess_messaage)
        logger.warning('Redirect to sign_in')
        return render(request, 'sign.in', {'messages': unsuccess_messaage})

    if (date_of_booking < date.today() or date_of_return < date_of_booking):
        unsuccess_message = 'Please give proper dates of booking!'
        logger.warning(unsuccess_message)
        logger.warning('Redirect to show_car_login')
        return render(request, 'show_car_login.html', {'unsuccess_message': unsuccess_message,
                                                       'car': current_car, 'customer': current_customer})

    total_days = (date_of_return - date_of_booking).days + 1
    total_price = total_days * current_car.price_per_day

    rent_data = {'date_of_booking': date_of_booking,
                 'date_of_return': date_of_return, 'total_days': total_days, 'total_price': total_price}

    if rent_cars.exists():

        for rent_car in rent_cars:
            if((date_of_booking < rent_car.date_of_booking and date_of_return <= rent_car.date_of_return) or
                    (date_of_booking >= rent_car.date_of_return and date_of_return > rent_car.date_of_return)):
                rent_car = RentCar(rent_car_brand=current_car.car_brand,
                                   rent_car_model=current_car.car_model,
                                   rent_car_plate=current_car.car_plate,
                                   date_of_booking=date_of_booking,
                                   date_of_return=date_of_return,
                                   total_days=total_days,
                                   total_price=total_price,
                                   customer_email=current_customer.customer_email,
                                   rent_status=True)

                available = True
                rent_car.save()
                logger.warning('Redirect to show_car_login')
                return render(request, 'show_car_login.html', {'Available': available, 'car': current_car,
                                                               'customer': current_customer, 'rent_data': rent_data})

            elif(rent_car.date_of_booking >= date_of_booking and date_of_return >= rent_car.date_of_return):
                unsuccess_message = f'Hi! Car is not available from {rent_car.date_of_booking} to {rent_car.date_of_return}.\
                                    So you can rent it from your date of booking till {rent_car.date_of_booking}\
                                    or from {rent_car.date_of_return} till your date of return'

                logger.warning(unsuccess_message)
                logger.warning('Redirect to show_car_login')
                return render(request, 'show_car_login.html', {'unsuccess_message': unsuccess_message,
                                                               'car': current_car, 'customer': current_customer})

            elif(rent_car.date_of_booking >= date_of_booking and date_of_return <= rent_car.date_of_return):
                unsuccess_message = f'Hi! Car is not available from {rent_car.date_of_booking} to {rent_car.date_of_return}.\
                                    So you can rent it from your date of booking till {rent_car.date_of_booking}'

                logger.warning(unsuccess_message)
                logger.warning('Redirect to show_car_login')
                return render(request, 'show_car_login.html', {'unsuccess_message': unsuccess_message,
                                                               'car': current_car, 'customer': current_customer})

            elif(rent_car.date_of_booking <= date_of_booking and date_of_return <= rent_car.date_of_return):
                unsuccess_message = f'Hi! Car is not available from {rent_car.date_of_booking} to {rent_car.date_of_return}.\
                                    Change the dates please'

                logger.warning(unsuccess_message)
                logger.warning('Redirect to show_car_login')
                return render(request, 'show_car_login.html', {'unsuccess_message': unsuccess_message,
                                                               'car': current_car, 'customer': current_customer})

    else:
        rent_car = RentCar(rent_car_brand=current_car.car_brand,
                           rent_car_model=current_car.car_model,
                           rent_car_plate=current_car.car_plate,
                           date_of_booking=date_of_booking,
                           date_of_return=date_of_return,
                           total_days=total_days,
                           total_price=total_price,
                           customer_email=current_customer.customer_email,
                           rent_status=True)

        available = True
        rent_car.save()
        logger.warning('Redirect to show_car_login')
        return render(request, 'show_car_login.html', {'Available': available, 'car': current_car,
                                                       'customer': current_customer, 'rent_data': rent_data})


def pageNotFound(request, exception):
    logger.warning('Page not found...')
    return HttpResponseNotFound(f'<h1>Page not found... </h1>')
