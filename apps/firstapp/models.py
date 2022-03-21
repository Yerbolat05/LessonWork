from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import (
    ValidationError,
)

from abstracts.models import (
    AbstractDateTime,
)
from django.db.models.query import QuerySet
from auths.models import CustomUser

class AccountQuerySet(QuerySet):
    def get_superuser(self) -> QuerySet:
        return self.filter(
            user__is_superuser = True
        )

class Account(AbstractDateTime):
    ACCOUNT_FULL_NAME_MAX_LENGTH = 20
    user = models.OneToOneField(
        CustomUser,
        on_delete = models.CASCADE  
    )
    full_name = models.CharField(max_length = ACCOUNT_FULL_NAME_MAX_LENGTH,verbose_name = 'Аккаунт')
    description = models.TextField()
    objects = AccountQuerySet().as_manager()

    def __str__(self):
        return f'Аккаунт : {self.user.id} / {self.full_name}'

    

    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Акакаунт'
        verbose_name_plural = 'Аккаунты'


# class GroupQuerySet(QuerySet):
#     HIGH_GPA_LEVEL = 4.0
#     def get_students_with_high_gpa(self) -> QuerySet:
#         return self.filter(
#             gpa__gt = self.HIGH_GPA_LEVEL
#         )

class Group(AbstractDateTime):
    GROUP_NAME_MAX_LENGTH = 10
    
    name = models.CharField(
        max_length = GROUP_NAME_MAX_LENGTH
    )

    # objects = GroupQuerySet().as_manager()

    def __str__(self) -> str:
        return f'Группа : {self.name}'
        
    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class StudentQuerySet(QuerySet):
    ADULT_AGE = 18
    def get_adult_students(self) -> QuerySet:
        return self.filter(
            age__gte=self.ADULT_AGE
        )

class Student(AbstractDateTime):
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

    objects = StudentQuerySet().as_manager()

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

class Proffessor(AbstractDateTime):
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

class HomeworkQuerySet(QuerySet):

    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=True
        )
    
class Homework(AbstractDateTime):
    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT
    )
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    logo = models.ImageField(
        'Лого домашней работы',
        upload_to='homework/',
        max_length=255
    )
    is_checked = models.BooleanField(default=False)

    objects = HomeworkQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.subject} | {self.title}'

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Домашняя работа'
        verbose_name_plural = 'Домашние работы'

class FileQuerySet(QuerySet):

    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=True
        )
    def get_select_homework(self) -> QuerySet:
        return self.filter(
            homework__is_checked = True
        )

class File(AbstractDateTime):
    homework = models.ForeignKey(
        Homework, on_delete=models.PROTECT
    )
    title = models.CharField(max_length=100)
    obj = models.FileField(
        'Объект файла',
        upload_to='homework_files/%Y/%m/%d/',
        max_length=255
    )

    objects = FileQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.homework.title} | {self.title}'

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'