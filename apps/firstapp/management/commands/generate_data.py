import random, names
from typing import Any 
from datetime import datetime 
 
from django.core.management.base import BaseCommand 
from django.conf import settings 
from django.contrib.auth.models import ( 
    User, 
) 
from django.contrib.auth.hashers import make_password 
 
from firstapp.models import ( 
    Group, 
    Account, 
    Student, 
    Proffessor, 
) 
 
 
class Command(BaseCommand): 
    """Custom command for filling up database. 
 
    Generate Test data only for database.  
    For each App you create another own Command 
    """ 
    help = 'Custom command for filling up database.' 
 
    def init(self, *args: tuple, **kwargs: dict) -> None: 
        pass 
 
         
    def _generate_users(self) -> None: 
        """Generate user account and student objects""" 
         
        USER_ACCOUNT_STUDENT_NUMBER = 500 
        SUPERUSER_LIMITED_COUNT = 1 
         
        def generate_email(first_name, last_name): 
            _email_patterns: tuple = ( 
                'gmail.com', 'outlook.com', 'yahoo.com', 
                'inbox.ru', 'inbox.ua', 'inbox.kz', 
                'yandex.ru', 'yandex.ua', 'yandex.kz', 
                'mail.ru', 'mail.ua', 'mail.kz', 
                ) 
            domain = random.choice(_email_patterns) 
            email_starter = f'{first_name}{last_name}' 
            email = f'{email_starter}@{domain}' 
            return email 
                 
         
        def generate_password(self): 
            password_pattern = 'abcde1234' 
            password = make_password(password_pattern) 
            return password  
         
        def generate_superuser(): 
            User.objects.create( 
                is_superuser = True, 
                is_staff = True, 
                username = 'nurya', 
                email = 'cat@mail.ru', 
                password = 'krymnevash', 
                first_name = 'Nuraziz', 
                last_name = 'Muhamedkali', 
            ) 
         
        users = User.objects.filter(is_superuser = False) 
        superadmins = User.objects.filter(is_superuser = True) 
        supersCount = len(superadmins) 
        userCount = len(users) 
        if supersCount < SUPERUSER_LIMITED_COUNT: 
            generate_superuser() 
             
        inc: int 
        for inc in range(USER_ACCOUNT_STUDENT_NUMBER - supersCount - userCount): 
            random_first_name: str = names.get_first_name() 
            random_last_name: str = names.get_last_name() 
            User.objects.create( 
                first_name = random_first_name, 
                last_name = random_last_name, 
                password = generate_password(self), 
                username = f'{random_first_name.lower()}{random_last_name.lower()}', 
                email = generate_email(random_first_name,random_last_name) 
            ) 
         
    # def _generate_groups(self) -> None:  
    #     """Generate Group objs.""" 
 
    #     def generate_name(inc: int) -> str: 
    #         return f'Группа {inc}' 
 
    #     inc: int 
    #     for inc in range(20): 
    #         name: str = generate_name(inc) 
    #         Group.objects.create( 
    #             name=name 
    #         ) 
 
    # def _generate_accounts_and_students(self) -> None: 
    #     """Generate Account objs.""" 
    #     pass 
     
    # def _generate_professors(self) -> None: 
    #     """Generate Professor objs.""" 
    #     pass 
 
    def handle(self, *args: tuple, **kwargs: dict) -> None: # Автоматически вызывается, когда вызывается generate_data файл 
        """Handles data filling.""" 
 
        start: datetime = datetime.now() # Получаем время в начале срабатывания кода, чтобы высчитать разницу 
 
        # self._generate_groups() # Генерируем данные 
        # self._generate_accounts_and_students() 
        # self._generate_professors() 
         
        self._generate_users() 
             
        # Выдаем время генерации данных 
        print( 
            'Generating Data: {} seconds'.format( 
                (datetime.now()-start).total_seconds()
            )
        )