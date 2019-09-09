from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=50)
    monthly_income = models.DecimalField(verbose_name=u'Renda Mensal', max_digits=9, decimal_places=2)
    current_score = models.IntegerField(verbose_name=u'Pontuação Atual', default=1)

    def __str__(self):
        return self.name



class Card(models.Model):
    client = models.ForeignKey(Client, verbose_name=u'Cliente', related_name='cards', on_delete=models.CASCADE)
    credit = models.CharField(verbose_name='Limite de Crédito', max_length=50)
    created_at = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.client, self.credit)
