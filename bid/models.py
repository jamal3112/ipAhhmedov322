from django.db import models

from cars.models import Driver

class Bid(models.Model):
    code_bid = models.CharField('Код заявки',max_length=20)
    phone_number = models.CharField('Номер телефона', max_length=11)
    time_bid = models.DateTimeField('Время заявки', auto_now = True )
    landing_area = models.CharField('Район посадки', max_length=20)
    end_landing_area = models.CharField('Район высадки', max_length=20)
    status = models.BooleanField('Выполнен')


    def __str__(self):
        return self.code_bid

    class Meta:
        verbose_name = 'Заявка',
        verbose_name_plural = 'Заявки'

class Street(models.Model):
    code_street = models.OneToOneField(Bid, on_delete=models.CASCADE)
    name_street = models.CharField('Название улицы', max_length=20)

    def __str__(self):
        return self.name_street
    
    class Meta:
        verbose_name = 'Улица',
        verbose_name_plural = 'Улицы'

class Area(models.Model):
    code_area = models.OneToOneField(Bid, on_delete=models.CASCADE)
    name_area = models.CharField('Название района', max_length=20)
    
    def __str__(self):
        return self.name_area
    
    class Meta:
        verbose_name = 'Район',
        verbose_name_plural = 'Районы'

class Location(models.Model):
    name_area = models.CharField('Локация', max_length=20, null=True,blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    driver = models.OneToOneField(Driver,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_area
    
    class Meta:
        verbose_name = 'Локация',
        verbose_name_plural = 'Локации'