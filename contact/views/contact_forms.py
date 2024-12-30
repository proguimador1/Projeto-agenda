from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import Contact 

def create(request):
    
    return render(
        request, 
        'contact/create.html',
        {}
        )