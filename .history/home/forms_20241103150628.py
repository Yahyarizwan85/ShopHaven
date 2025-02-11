# forms.py
from django import forms
from .customer import Customer

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'bio', 'profile_picture']
