from rest_framework.viewsets import ModelViewSet
from credit_card.models import Client, Card
from .serializers import ClientSerializer, CardSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
