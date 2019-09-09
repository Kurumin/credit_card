from django.shortcuts import render
from .forms import ClientForm
from .models import Client, Card
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'index.html')


def clients(request):
    clients_list = Client.objects.all()
    form = ClientForm()
    return render(request, 'clients.html', locals())


def client_detail(request, pk):
    client = get_object_or_404(Client,pk=pk)
    form = ClientForm(instance=client)
    return render(request, 'client_dashboard.html', locals())


def cards(request, client_id):
    client = Client.objects.get(id=client_id)
    cards_list = Card.objects.all()
    return render(request, 'cards.html', locals())
