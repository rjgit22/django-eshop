from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')

        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First name required"
        elif len(customer.first_name) < 4:
            error_message = "must greater than 4 digits"
        elif not customer.last_name:
            error_message = "Last name required"
        elif len(customer.last_name) < 2:
            error_message = "must greater than 2 digits"
        elif not customer.phone:
            error_message = "Phone number required"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be of 10 digits"
        elif not customer.password:
            error_message = "Required password"
        elif len(customer.password) < 6:
            error_message = "Password must be 6 digits long"
        elif customer.isexists():
            error_message = 'Email already registered'

        return error_message
