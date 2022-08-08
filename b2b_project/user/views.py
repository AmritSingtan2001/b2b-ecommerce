from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from shop.decorators import admin_required
from .mixins import CustomSignupView
from .models import Customer, Salesman, Admin
from .forms import AdminSignupForm, CustomerSignupForm, SalesmanSignupForm

class CustomerSignupView(CustomSignupView):
   success_url = 'account_login'
   profile_class = Customer
   form_class = CustomerSignupForm
   template_name = 'account/signup.html'


class SalesmanSignupView(CustomSignupView):
    success_url = 'account_login'
    profile_class = Salesman
    form_class = SalesmanSignupForm
    template_name = 'account/salesman_signup.html'

class AdminSignupView(CustomSignupView):
    success_url = 'account_login'
    profile_class = Admin
    form_class = AdminSignupForm