from django.db import models
from django.core.validators import RegexValidator

class Credit(models.Model):
    limit_score = models.IntegerField(verbose_name=u'Score Limite')
    credit = models.CharField(verbose_name='Crédito se condição satisfeita', max_length=30,
                              help_text="Deve ser somente o termo '\"Reprovado\"' ou 'renda', números e operadores aritméticos(+-/*)",
                              validators=[RegexValidator('^"Reprovado"|((renda|[0-9]+)([\+-\/\*](renda|[0-9]+))?)$', message="Deve ser somente o termo 'renda', números e operadores aritméticos")])
    condition = models.CharField(verbose_name='Condição', max_length=20,
                                 help_text="Deve ser somente o termo 'renda', números e operadores de comparação(>=<)",
                                 validators=[RegexValidator('^(renda|[0-9]+)([>=<]{1,2}(renda|[0-9]+))$', message="Deve ser somente o termo 'renda', números e operadores aritméticos")], null=True, blank=True)
    credit_condition = models.CharField(verbose_name='Crédito se condição não satisfeita', max_length=30,
                                        help_text="Deve ser somente o termo '\"Reprovado\"' ou 'renda', números e operadores aritméticos(+-/*)",
                                        validators=[RegexValidator('^"Reprovado"|((renda|[0-9]+)([\+-\/\*](renda|[0-9]+))?)$', message="Deve ser somente o termo 'renda', números e operadores aritméticos")], default='"Reprovado"', null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.limit_score)


class Client(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=50)
    email = models.EmailField(verbose_name=u'Email', null=True)
    cpf = models.CharField(verbose_name=u'CPF', max_length=14, null=True)
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
