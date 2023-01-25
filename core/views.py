from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def home(request):

    return render(request, 'core/home.html',{'home':'active'})


def contact(request):
    form = ContactForm()
    return render(request, 'core/contact.html', {'form':form})

