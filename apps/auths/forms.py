from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from auths.models import CustomUser

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