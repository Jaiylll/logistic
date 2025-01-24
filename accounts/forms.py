from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''
    )
    phone_number = forms.CharField(
        label='Моб. телефон',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    passport_pin = forms.CharField(
        label='ИИН',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'phone_number', 'passport_pin', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': '',
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username': ''
        }
        labels = {
            'username': 'Имя пользователя',  # Задаём метку для поля username
            'password': 'Пароль',  # Задаём метку для поля password
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
        }
