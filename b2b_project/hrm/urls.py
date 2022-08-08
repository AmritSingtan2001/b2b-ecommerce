from django.urls import path

from . import views

app_name = 'hrm'
urlpatterns = [ 
    path('admin-dashboard/employees/', views.employee_list, name = 'employee_list'),
    path('admin-dashboard/employees/add/', views.add_employee, name = 'add_employee'),
    path('admin-dashboard/employees/delete/<int:id>/', views.delete_employee, name = 'delete_employee'),
    path('admin-dashboard/employees/attendance/', views.add_attendance, name = 'attendance'),
]