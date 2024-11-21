from django.shortcuts import render

# Create your views here.
def initial(request):
    return render(request, 'contact/index.html')