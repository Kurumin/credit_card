from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from credit_card.models import Client, Card
from .serializers import ClientSerializer, CardSerializer
from rest_framework import status
from rest_framework.response import Response
import locale
locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")


import random

limit_credit = {
    299: lambda income: 'Reprovado',
    599: lambda income: locale.currency(1000),
    850: lambda income: locale.currency(income/2 if income > 2000 else 1000),
    950: lambda income: locale.currency(income*2),
    999: lambda income: locale.currency(1000000)
}


def get_score():
    return random.randint(1, max(limit_credit))


def get_limit(score):
    for limit_group in sorted(limit_credit):
        if limit_group >= score:
            return limit_group


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def partial_update(self, request, pk=None):
        client = get_object_or_404(Client, pk=pk)
        client.current_score = get_score()
        client.save()
        serializer = ClientSerializer(client)
        return Response(serializer.data)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        client = get_object_or_404(Client, pk=kwargs['client'])
        card = Card(client_id=client.id, credit=limit_credit[get_limit(client.current_score)](client.monthly_income))
        card.save()
        return Response(self.get_serializer(card).data, status=status.HTTP_201_CREATED, headers=headers)


    def get_queryset(self):
        try:
            client_id = self.kwargs['client']
            return Card.objects.filter(client_id__exact=client_id)
        except:
            return Card.objects.all()
