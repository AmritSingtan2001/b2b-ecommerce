from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Credit
from shop.decorators import admin_required


@login_required
@admin_required
def list_credits(request):
    credits = Credit.objects.all()
    return render(request, 'accounting/credit_list.html', {'credits':credits})