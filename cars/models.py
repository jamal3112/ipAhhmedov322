from django.db import models

class Car(models.Model):
    brand = models.CharField('Марка машины',max_length=20)
    color = models.CharField('Цвет машины', max_length=20)
    state_number = models.CharField('Государсвенный номерной знак', max_length=9)

    LOAN_STATUS = (
        ('r', 'repairs'),
        ('w', 'work'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='w')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Машина',
        verbose_name_plural = 'Машины'

class CarBrand(models.Model):
    brand_сode = models.ForeignKey(Car, on_delete=models.CASCADE)
    brand = models.CharField('Модель машины', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.brand
    
    class Meta:
        verbose_name = 'Модель машины',
        verbose_name_plural = 'Модели машин'

class Driver(models.Model):
    have_car = models.OneToOneField(Car, on_delete=models.CASCADE, null=True,blank=True)
    callsign = models.CharField('Позывной', max_length=20)
    lastname = models.CharField('Фамилия',max_length=20 )
    date_of_birth = models.DateField('Дата рождения', max_length=20)
    work_experience = models.IntegerField('Стаж работы')

    LOAN_STATUS = (
        ('n', 'not on line'),
        ('y', 'on the line'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='y')

    
    def __str__(self):
        return self.callsign
    
    class Meta:
        verbose_name = 'Водитель',
        verbose_name_plural = 'Водители'