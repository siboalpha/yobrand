from array import array
from dataclasses import field
from statistics import mode
from django import forms
from django.forms import ModelForm, TextInput, Select, Textarea, SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Activity, Employee, Task, Request

class CreateEmployeeForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'form-control','placeholder': 'username'})
        self.fields["first_name"].widget.attrs.update({'class': 'form-control','placeholder': 'First name'})
        self.fields["last_name"].widget.attrs.update({'class': 'form-control','placeholder': 'Last name'})
        self.fields["email"].widget.attrs.update({'class': 'form-control','placeholder': 'Email'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control','placeholder': 'Password'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control','placeholder': 'Confirm passowrd'})
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']

class DatePickerInput(forms.DateInput):
        input_type = 'date'
class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'employee', 'project', 'description', 'due_date', 'due_time']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Task title'}),
            'employee': Select(attrs={'class': 'form-control'}),
            'project': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'due_date': DatePickerInput(attrs={'class': 'form-control'}),
            'due_time': TimePickerInput(attrs={'class': 'form-control'})

        }

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['username','phone','birthday', 'gender', 
                'position', 'address', 'address2', 'country',
                'state_city', 'eduction']
        widgets = {
            'username': Select(attrs={'class': 'form-control', 'placeholder':'Phone Number'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder':'Phone Number'}),
            'gender': Select(attrs={'class': 'form-control', 'placeholder':'Gender'}),
            'birthday':SelectDateWidget(attrs={'class': 'form-control'}),
            'position': TextInput(attrs={'class': 'form-control', 'placeholder':'Work position'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder':'Primary address'}),
            'address2': TextInput(attrs={'class': 'form-control', 'placeholder':'Secondry address'}),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder':'Your country'}),
            'state_city': TextInput(attrs={'class': 'form-control', 'placeholder':'State or city'}),
            'eduction': TextInput(attrs={'class': 'form-control', 'placeholder':'Education level'}),
        }

class AddActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'due_date']
        widgets = {
        'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity title'}),
        'due_date': DatePickerInput(attrs={'class': 'form-control'}),
        'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Activity description'}),

    }


class SubmitRequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'request_to']
        widgets = {
        'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity title'}),
        'request_to': Select(attrs={'class': 'form-control'}),
        'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Activity description'}),

    }
