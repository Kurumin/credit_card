from django.shortcuts import render
from .forms import ClientForm
from .models import Client
# Create your views here.

def home(request):
    return render(request, 'index.html')


def clients(request):
    clients_list = Client.objects.all()
    form = ClientForm()
    return render(request, 'clients.html', locals())
