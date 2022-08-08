from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Department(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 100)
    designation = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    contact_no = PhoneNumberField(max_length = 15)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    joined_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.full_name

    def get_per_day_salary(self):
        return self.salary/24


class Date(models.Model):
    date = models.DateField(default=timezone.now, unique=True)

    def __str__(self):
        return self.date


class Attendance(models.Model):
    STATUS_CHOICES = (('absent','Absent'),('present','Present'))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    date = models.ForeignKey(Date, related_name='attendance', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15)
    first_in = models.TimeField(blank=True, null=True, default=timezone.now)
    last_out = models.TimeField(blank=True, null=True, default=timezone.now)

    #class Meta:
    #    unique_together = ('employee','date')

