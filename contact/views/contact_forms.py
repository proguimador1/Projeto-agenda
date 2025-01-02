from django.shortcuts import render
from ..forms import ContactForm


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