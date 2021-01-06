from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse

from utils.email import send_confirmation_email
from utils.token import account_activation_token

from . import forms

User = get_user_model()


def register(request):
    ''' Регистрация пользователя  '''

    context = {}
    if request.POST:
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = False
            user.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            # Отправляем почту чтобы юзеп подтвердил емайл
            send_confirmation_email(request, user)

            account = authenticate(email=email, password=password)
            auth_login(request=request, user=account)
            return redirect('post:list')
        else:
            context['form'] = form
    else:
        form = forms.CreateUserForm()
        context['form'] = form
        print(context)


    return render(request, 'accounts/registration.html', context)


def activate(request, uidb64, token):
    ''' User account activation view '''

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None


    if user is not None and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        auth_login(request, user)
        return redirect('post:list')
    else:
        return HttpResponse('Ссылка для активации аккаунта недействительна!')


def logout(request):
    ''' User logout view '''

    auth_logout(request)
    return redirect('post:list')


def login(request):
    ''' User login view '''

    user = request.user
    context = {}

    if request.POST:
        form = forms.AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                auth_login(request, user)
                return redirect('post:list')
        else:
            context['form'] = form
    else:
        form = forms.AccountAuthenticationForm()
        context['form'] = form
    return render(request, 'accounts/login.html', context)
