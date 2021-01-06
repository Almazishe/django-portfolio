from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


# Модель юзера
User = get_user_model()


class CreateUserForm(UserCreationForm):
    """ Форма создания юзера """

    email = forms.EmailField(label='Электронная почта', max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'email',
            'phone_number',
            'password1',
            'password2'
        )

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "password")

    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Неверный логин или пароль")

