from django.contrib import admin

from .models import User, Salesman, Customer, Admin

admin.site.register(User)
admin.site.register(Salesman)
admin.site.register(Customer)
admin.site.register(Admin)