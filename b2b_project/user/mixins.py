from allauth.account.views import SignupView
#from .forms import CustomSignupForm
from .models import Customer, Admin, Salesman

from django.db import transaction


class CustomSignupView(SignupView):
  template_name = ''
  success_url = ''  # profile specific success url
  form_class = None
  profile_class = None  # profile class goes here

  def form_valid(self, form):
    response = super(CustomSignupView, self).form_valid(form)
    user_type = self.profile_class(user=self.user, 
                                   full_name = form.cleaned_data['full_name'],
                                   address = form.cleaned_data['address'],
                                   contact_no = form.cleaned_data['contact_no'])
    user_type.save()

    return response