from django.db import models
import datetime

year_choices = [(y, y) for y in range(1920, datetime.date.today().year+1)]

class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО')
    citizenship = models.CharField(max_length=20, blank=True, default='Кыргызстан', verbose_name='Гражданство')
    # к полю birth_year. если  нужен только год подумал, может вместо datafield так показать:
    birth_year = models.IntegerField(verbose_name='Год рождения', choices=year_choices)
    work_place = models.CharField(max_length=30, blank=True, null=True, verbose_name='Место работы')
    update_date = models.DateField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'

    def __str__(self):
        return f' {self.name}; {self.birth_year} г.р.'


class Account(models.Model):
    number = models.CharField(max_length=16,unique=True, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1, blank=True, verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return f'{self.number}; {self.account_type}'


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита')
    date = models.DateField(verbose_name='Дата получения кредита', auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Cчет')

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
        db_table = 'loans'

    def __str__(self):
        return f'{self.sum}; {self.date}'

