from django.shortcuts import render
from ..models import Contact 

# Create your views here.
def initial(request):
    contacts = Contact.objects.all()

    return render(
        request, 
        'contact/index.html',
        {'contacts': contacts}
        )