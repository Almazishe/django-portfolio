from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserView(CreateView):
    """ Создание юзера """

    model = User
    # succ