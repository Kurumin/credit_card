from django.db import models
import random
# Create your models here.


class Client(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=50)
    email = models.EmailField(verbose_name=u'Email')
    cpf = models.CharField(verbose_name=u'CFP', max_length=14)
    monthly_income = models.DecimalField(verbose_name=u'Renda Mensal', decimal_places=2)
    current_score = models.IntegerField(verbose_name=u'Pontuação Atual', default=random.randint(1, 999))

    def __str__(self):
        return self.name



class Card(models.Model):
    client = models.ForeignKey(Client, verbose_name=u'Cliente', on_delete=models.CASCADE)
    credit = models.CharField(verbose_name='Limite de Crédito', max_length=50)
    created_at = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.client, self.credit)
