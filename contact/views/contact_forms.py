from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ..forms import ContactForm
from ..models import Contact


def create(request):
    form_action = reverse('contact:create')

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
        'form': form,
        'form_action': form_action
        }
        )
        
    return render(
        request, 
        'contact/create.html',
        {
        'site_title': 'Create contact',
        'form': ContactForm(),
        'form_action': form_action
        }
        )

def update(request, contact_id):
    contact = get_object_or_404(Contact, id = contact_id, show = True)

    form_action = reverse('contact:update', args = (contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('/')

        return render(
        request, 
        'contact/create.html',
        {
        'site_title': 'Create contact',
        'form': form,
        'form_action': form_action
        }
        )
        
    return render(
        request, 
        'contact/create.html',
        {
        'site_title': 'Update contact',
        'form': ContactForm(),
        'form_action': form_action
        }
        )