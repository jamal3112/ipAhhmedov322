from django.db import models

from cars.models import Driver
from bid.models import Bid

class ServiceBid(models.Model):
    code_bid = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True, blank=True)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    time_start = models.DateTimeField('Время начала поездки', auto_now = True )
    time_end = models.CharField('Время окончания поездки', max_length=20)
    


    def __str__(self):
        return str(self.code_bid)

    class Meta:
        verbose_name = 'Обслуживание заявки',
        verbose_name_plural = 'Обслуживание заявок'

class TaximeterValue(models.Model):
    code_bid = models.ForeignKey(ServiceBid, on_delete=models.CASCADE)
    code_parameter = models.CharField('Код парамерта', max_length=20)

    def __str__(self):
        return self.code_parameter
    
    class Meta:
        verbose_name = 'Значение таксометра',
        verbose_name_plural = 'Значения таксометров'

class TaximeterTarif(models.Model):
    code_parameter = models.ForeignKey(TaximeterValue, on_delete=models.CASCADE)
    parameter_unit = models.IntegerField('Еденица измерения параметра')
    price = models.IntegerField('Цена')
    LOAN_STATUS = (
        ('Стандарт', 'Стандарт'),
        ('Комфорт', 'Комфорт'),
        ('Бизнес', 'Бизнес'),
    )

    tarif = models.CharField(max_length=10, choices=LOAN_STATUS, blank=True, default='Стандарт')

    
    def __str__(self):
        return self.tarif
    
    class Meta:
        verbose_name = 'Тариф таксометра',
        verbose_name_plural = 'Тарифы таксометров'

