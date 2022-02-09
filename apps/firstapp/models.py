from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import (
    ValidationError,
)

class Account(models.Model):
    ACCOUNT_FULL_NAME_MAX_LENGTH = 20
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE  
    )
    full_name = models.CharField(max_length = ACCOUNT_FULL_NAME_MAX_LENGTH,verbose_name = 'Аккаунт')
    description = models.TextField()

    def __str__(self):
        return f'Аккаунт : {self.user.id} / {self.full_name}'

    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Акакаунт'
        verbose_name_plural = 'Аккаунты'

class Group(models.Model):
    GROUP_NAME_MAX_LENGTH = 10
    
    name = models.CharField(
        max_length = GROUP_NAME_MAX_LENGTH
        )
    def __str__(self) -> str:
        return f'Группа : {self.name}'
        
    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'



class Student(models.Model):
    MAX_AGE = 27
    account = models.OneToOneField(
        Account,
        on_delete = models.CASCADE,
        verbose_name = 'Аккаунт'
    )
    age = models.IntegerField(
        'Возраст студета'
    )
    group = models.ForeignKey(
        Group,
        on_delete = models.PROTECT,
        verbose_name = 'Группа'
    )
    gpa = models.FloatField(
        'Средняя оценка'
    )
    def __str__(self) -> str:
        return f'Имя : {self.account.full_name} - Возраст : {self.age} - {self.group} - Оценка : {self.gpa}'
    
    def save(
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None:
        if self.age > self.MAX_AGE:
            #v1
        #     self.age = self.MAX_AGE
        

        #v2
            raise ValidationError(
                f'Допустимый возраст : {self.MAX_AGE}'
            )
        super().save(*args,**kwargs)
        
    class Meta:
        ordering = (
            'account',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Proffessor(models.Model):
    FULL_NAME_MAX_LENGTH = 20

    TOPIC_JAVA = 'Java'
    TOPIC_PYTHON = 'python'
    TOPIC_TYPESCRIPT = 'Typescript'
    TOPIC_JAVASCRIPT = 'Javascript'
    TOPIC_RUBY = 'Ruby'
    TOPIC_GOLAND = 'Goland'
    TOPIC_SQL = 'Sql'
    TOPIC_SWIFT = 'swift'

    TOPIC_CHOICES = (
        {TOPIC_JAVA,'JAVA'},
        {TOPIC_PYTHON,'Python'},
        {TOPIC_TYPESCRIPT,'JavaScript'},
        {TOPIC_RUBY,'TypeScript'},
        {TOPIC_GOLAND,'Ruby'},
        {TOPIC_SQL,'Golang'},
        {TOPIC_SWIFT,'SQL'},
        {TOPIC_SWIFT,'Swift'},
    )
    full_name = models.CharField(
        verbose_name = 'полное имя',
        max_length = FULL_NAME_MAX_LENGTH,
    )
    topic = models.CharField(
        verbose_name = 'предмет',
        choices = TOPIC_CHOICES,
        default = TOPIC_JAVA,
        max_length = FULL_NAME_MAX_LENGTH,
    )
    students = models.ManyToManyField(
        Student
    )

    def __str__(self) -> str:
        return f'Имя : {self.full_name}  -- Организация : {self.topic}'

    def save(
        self,
        *args: tuple,
        **kwargs:dict,
    ) -> None:
        if self.topic is None:
            raise ValidationError(
                f"Вы не выбрали свою организвцию"
            )
        super().save(*args,**kwargs)
    
    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Проффессор'
        verbose_name_plural = 'Проффессоры'
