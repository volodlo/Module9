from django.db import models
from django.urls import reverse


class Company(models.Model):

    name_company = models.CharField(max_length=20, db_index=True, verbose_name='Название кампании')

    def get_absolute_url(self):
        return reverse('company', kwargs = {'company_id': self.pk})

    def __str__(self):
        return self.name_company

    class Meta:
        verbose_name_plural = 'Кампании'
        verbose_name = 'Кампания'


class Human(models.Model):

    name = models.CharField( verbose_name='Имя', max_length=50)
    surname = models.CharField( verbose_name='Фамилия', max_length=50)
    mail = models.EmailField( verbose_name='Адрес электронной почты', max_length=50)
    telephone = models.IntegerField( verbose_name='Номер телефона')
    c = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Кампания')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_id': self.c.pk})


class House(models.Model):

    city = models.CharField('Город', max_length=50)
    street = models.CharField('Улица',  max_length=50)
    house_number = models.IntegerField('Номер дома', null=True, blank=True,)
    c = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Кампания')

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_id': self.c.pk})
