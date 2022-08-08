from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField
from django import forms

class CustomerSignupForm(SignupForm):
    full_name = forms.CharField(max_length=100, label = 'Full Name')
    contact_no = PhoneNumberField(label = "Contact No.")
    address = forms.CharField(max_length=200, label = 'Address')

    def save(self, request,):
        user = super(CustomerSignupForm, self).save(request)
        user.is_customer = True
        user.is_active = False
        user.save()
        return user

class SalesmanSignupForm(SignupForm):
    full_name = forms.CharField(max_length=100, label = 'Full Name')
    contact_no = PhoneNumberField(label = "Contact No.")
    address = forms.CharField(max_length=200, label = 'Address')

    def save(self, request,):
        user = super(SalesmanSignupForm, self).save(request)
        user.is_salesman = True
        user.is_active = False
        user.save()
        return user

class AdminSignupForm(SignupForm):
    full_name = forms.CharField(max_length=100, label = 'Full Name')
    contact_no = PhoneNumberField(label = "Contact No.")
    address = forms.CharField(max_length=200, label = 'Address')

    def save(self, request,):
        user = super(AdminSignupForm, self).save(request)
        user.is_admin = True
        user.save()
        return user