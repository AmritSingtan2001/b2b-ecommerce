from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from shop.decorators import admin_required
from .forms import AddEmployeeForm, AttendanceFormset, AttendanceForm
from .models import Employee, Attendance, Date

@login_required
@admin_required
def employee_list(request):
    employee_list = Employee.objects.all()
    return render(request, 'hrm/employee_list.html', {'employee_list':employee_list})


@login_required
@admin_required
def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hrm:employee_list')
        else:
            return HttpResponse("Invalid Form")    
    else:
        form = AddEmployeeForm() 
    return render(request, 'hrm/add_employee.html', {'form':form})


@login_required
@admin_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id = employee_id)
    employee.delete()
    return redirect('hrm:employee_list')


@login_required
@admin_required
def add_attendance(request):
    employee_list = Employee.objects.all()
    if request.method == 'POST':
        date = Date.objects.create(date = request.POST['date'])
        date.save()
        for x in range(1,len(employee_list)+1):
            employee = employee_list[x-1]
            status = request.POST[f'option{x}']
            first_in = request.POST[f'in-time{x}']
            last_out = request.POST[f'in-time{x}']
            attendance = Attendance(date=date,
                                    employee=employee,
                                    status=status,
                                    first_in=first_in,
                                    last_out=last_out)
            attendance.save()

    return render(request, 'hrm/attendance.html', {'employee_list':employee_list})