from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from auths.models import CustomUser
from django import forms 


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )

    
class CustomUserChangeFrom(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )

class CustomUserForm(forms.ModelForm):
    email = forms.EmailField(label='Электронная почта')
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль'
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password'
        )