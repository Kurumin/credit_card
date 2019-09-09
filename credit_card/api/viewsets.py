from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from credit_card.models import Client, Card, Credit
from .serializers import ClientSerializer, CardSerializer
from rest_framework import status
from rest_framework.response import Response
import locale
import random


locale.setlocale(locale.LC_ALL, "pt_BR.utf8")


limit_credit = {
    299: eval('lambda renda: "Reprovado"'),
    599: eval('lambda renda: locale.currency(1000)'),
    850: eval('lambda renda: locale.currency(renda/2) if renda>2000 else locale.currency(1000)'),
    950: eval('lambda renda: locale.currency(renda*2)'),
    999: eval('lambda renda: locale.currency(1000000)')
}


def get_limit_rules():
    limit_credit_obj = dict()
    for credit in Credit.objects.all():
        function_str = 'lambda renda: '
        if credit.credit != '"Reprovado"':
            function_str += 'locale.currency({})'.format(credit.credit)
        else:
            function_str += '{}'.format(credit.credit)
        if credit.condition:
            function_str += ' if {} else '.format(credit.condition)
            if credit.credit_condition != '"Reprovado"':
                function_str += 'locale.currency({})'.format(credit.credit_condition)
            else:
                function_str += '{}'.format(credit.credit_condition)
        limit_credit_obj[int(credit.limit_score)] = eval(function_str)

    return limit_credit_obj


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
        limit_credit_array = get_limit_rules()
        client = get_object_or_404(Client, pk=kwargs['client'])
        card = Card(client_id=client.id, credit=limit_credit_array[get_limit(client.current_score)](client.monthly_income))
        card.save()
        return Response(self.get_serializer(card).data, status=status.HTTP_201_CREATED, headers=headers)


    def get_queryset(self):
        try:
            client_id = self.kwargs['client']
            return Card.objects.filter(client_id__exact=client_id)
        except:
            return Card.objects.all()
