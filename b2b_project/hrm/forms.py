from django import forms

from .models import Attendance, Employee


class AddEmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update({'class': 'form-select'})
        self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['designation'].widget.attrs.update({'class': 'form-control'})
        self.fields['salary'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Employee
        fields = ['department', 'full_name', 'designation', 'salary', 'contact_no', 'email', 'address']


class AttendanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs.update({'class': 'form-select'})
        #self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_in'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_out'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Attendance
        fields = ('employee', 'status', 'first_in', 'last_out')

AttendanceFormset = forms.formset_factory(form=AttendanceForm, extra=Employee.objects.count())
