from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class EmployeeForm(UserCreationForm):
    
    fname = forms.CharField()
    lname = forms.CharField()
    img = forms.ImageField()
    contact = forms.IntegerField()
    email = forms.EmailField()
    o_id = forms.IntegerField()
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        o_id = int(self.cleaned_data.get('o_id'))
        print(o_id)
        o = Owner.objects.get(id=o_id)
        employee = Employee.objects.create(user=user,owner=o)
        
        employee.fname=self.cleaned_data.get('fname')
        
        employee.lname=self.cleaned_data.get('lname')
        employee.img=self.cleaned_data.get('img')
        employee.contact= int(self.cleaned_data.get('contact'))
        print(employee.contact)
        employee.email=self.cleaned_data.get('email')
        employee.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


