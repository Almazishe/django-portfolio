from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Модель юзера
User = get_user_model()


class CreateUserForm(UserCreationForm):
    """ Форма создания юзера """

    email = forms.EmailField(label='Электронная почта', )






