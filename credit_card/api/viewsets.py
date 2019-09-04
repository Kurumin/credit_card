from rest_framework.viewsets import ModelViewSet
from credit_card.models import Client, Card

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializers_class = ClientSerializer
