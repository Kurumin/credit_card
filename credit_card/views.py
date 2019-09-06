from django.shortcuts import render
from .forms import ClientForm
# Create your views here.

def home(request):
    return render(request, 'index.html')


def clients(request):
    form = ClientForm()
    return render(request, 'clients.html', locals())
