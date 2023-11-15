from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ModelForm, NumberInput

from users.models import ProfileUser


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = ProfileUser
        fields = ('username', 'email', 'name', 'surname', 'date_of_birth', 'gender')

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    date_of_birth = forms.DateField(label='Дата рождения', widget=NumberInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(label='Выберите пол',  choices=ProfileUser.GENDER)


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = ProfileUser
        fields = ('username', 'email', 'name', 'surname', 'date_of_birth', 'gender')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

