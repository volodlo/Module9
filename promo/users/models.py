from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class ProfileUser(AbstractUser):
	GENDER = (
		("Мужской", "Мужской"),
		("Женский","Женский"),
		)
	email = models.EmailField(max_length=50, verbose_name='Email', blank=True, unique=True)
	name = models.CharField(max_length=20, verbose_name='Имя')
	surname = models.CharField(max_length=20, verbose_name='Фамилия')
	date_of_birth = models.DateField(max_length=20, verbose_name='Дата рождения', null=True)
	gender = models.CharField(max_length=20, verbose_name='Выберите пол', choices=GENDER)
	password1 = models.CharField(max_length=20, verbose_name='Пароль')
	password2 = models.CharField(max_length=20, verbose_name='Повторите пароль')

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('profile', kwargs={'current_user': self.pk})