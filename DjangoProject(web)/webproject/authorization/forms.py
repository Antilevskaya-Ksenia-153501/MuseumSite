from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import CustomUser, Employee, Customer
from datetime import date
from typing import Any


def validate_age(item):
    today = date.today()
    age = today.year - item.year - int((today.month, today.day) < (item.month, item.day))
    if int(age) < 18:
        raise ValidationError('You must be over 18 y.o.')


class EmployeeCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date_birth = forms.DateField(validators=[validate_age])
    phone_number = forms.CharField(max_length=50, help_text='Format +375 (29) XXX-XX-XX',
                                   validators=[RegexValidator(
                                       regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
                                       message='Format +375 (29) XXX-XX-XX', )])

    class Meta:
        model = Employee
        fields = [
            'username', 'email', 'first_name',
            'last_name', 'date_birth',
            'phone_number', 'image', 'post','password1',
            'password2'
        ]

    def save(self, commit: bool):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_birth = self.cleaned_data['date_birth']
        user.phone_number = self.cleaned_data['phone_number']
        user.post = self.cleaned_data['post']
        user.is_employee = True
        if commit:
            user.save(True)
        return user


class CustomerCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Customer
        fields = [
            'username', 'email', 'password1',
            'password2'
        ]

    def save(self, commit: bool):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_customer = True
        if commit:
            user.save(True)
        return user