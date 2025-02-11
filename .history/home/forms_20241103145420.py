# forms.py
from django import forms
from .models import Profile  # or Customer if using that model

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # or Customer
        fields = ['bio', 'profile_picture']  # Add fields you want to allow users to edit
