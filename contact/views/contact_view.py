from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import Contact 

def initial(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, 
        'contact/index.html',
        {'page_obj': page_obj,
        'site_title': 'Agenda'}
        )

def search(request):
    search_value = request.GET.get('q', '').strip(' ')

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value)).order_by('-id')
    
    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, 
        'contact/index.html',
        {'page_obj': page_obj,
        'site_title': 'Agenda'}
        )

def contact(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id, show=True)
    site_tile = f'{single_contact.first_name} {single_contact.last_name}'

    return render(
        request, 
        'contact/contact.html',
        {'contact': single_contact,
        'site_title': site_tile}
        )