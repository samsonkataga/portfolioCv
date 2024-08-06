from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['fullname','email','message']