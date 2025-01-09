from django.shortcuts import render, redirect
from ..forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

        return render(
        request, 
        'contact/create.html',
        {
        'site_title': 'Create contact',
        'form': form
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