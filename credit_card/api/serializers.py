from rest_framework.serializers import ModelSerializer
from credit_card.models import Client, Card


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'