from django import forms
from django.forms import ModelForm, TextInput, Select, Textarea, SelectDateWidget, URLInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

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
            'birthday':DatePickerInput(attrs={'class': 'form-control'}),
            'position': Select(attrs={'class': 'form-control', 'placeholder':'Work position'}),
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

class SubmitRequest(ModelForm):
    class Meta:
        model = EmployeeRequest
        fields = ['title','to_user', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Request title'}),
            'to_user': Select(attrs={'class': 'form-control', 'placeholder': 'Request title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Request details'}),
        }

    

class addClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'website', 'instagram', 'facebook', 'twitter', 'linkedin']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Clients name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Clients email'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Clients phone'}),
            'website': URLInput(attrs={'class': 'form-control', 'placeholder': 'Clients website'}),
            'instagram': URLInput(attrs={'class': 'form-control', 'placeholder': 'Clients instagram'}),
            'facebook': URLInput(attrs={'class': 'form-control', 'placeholder': 'Clients facebook'}),
            'twitter': URLInput(attrs={'class': 'form-control', 'placeholder': 'Clients twitter'}),
            'linkedin': URLInput(attrs={'class': 'form-control', 'placeholder': 'Clients linkedin'}),

        }