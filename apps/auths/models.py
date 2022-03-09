from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        email: str,
        password: str,
        **kwargs: dict
    ) -> 'CustomUser':
        if not email:
            raise ValidationError('Email required')
            
        email: str = self.normalize_email(email)
        user: 'CustomUser' = self.model(
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        **kwargs: dict
    ) -> 'CustomUser':
        is_staff = True

        return self.create_user(
            email,
            password,
            **kwargs
        )

    #     def __str__(self):
    #         return f'Пользователь : {self.email}'

    #     def save(self,*args,**kwargs) -> None:
    #         if(self.email != self.email.lower()):
    #             raise ValidationError(
    #                 'Ваш email "{self.email}" должен быть в нижнем регистре',
    #                 code = 'lower_case_email_error',
    #                 params = {'email': self.email}
    #             )
    #         super().save(*args,**kwargs)
            
    # class Meta:
    #     ordering = (
    #         'email'
    #     )
    #     verbose_name = 'Электронная почта'
    #     verbose_name_plural = 'Электронные почты'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Почта/Логин', unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    datetime_joined = models.DateTimeField(
        verbose_name = 'время регестрации',
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = (
            'datetime_joined',
        )
        verbose_name = 'Польователь'
        verbose_name_plural = 'Пользователи'

    

