from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.db.models import Q
from ..models import Contact 
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone',

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Error message',
                code='Invalid'
            )
        )

        return super().clean()

def create(request):
    if request.method == 'POST':
        return render(
        request, 
        'contact/create.html',
        {
        'site_title': 'Create contact',
        'form': ContactForm(request.POST)
        }
        )
        
    return render(
        request, 
        'contact/create.html',
        {
        'site_title': 'Create contact',
        'form': ContactForm()
        }
        )