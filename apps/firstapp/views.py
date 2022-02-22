from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import (
    Account,
    Student,
)

def index(request: WSGIRequest) -> HttpResponse:
    """Search First User"""
    user : User = User.objects.first()
    name : str = user.first_name

    account : Account = user.account
    name_account : str = account.full_name

    student : Student = account.student
    gpa : int = student.gpa

    text: str = f'Name: {name}<br> Account: {name_account}<br>GPA: {gpa}'

    response: HttpResponse = HttpResponse(text)

    return response

def index_2(request: WSGIRequest) -> HttpResponse:
    """Start Page"""
    return HttpResponse(
        '<h1>Страница : Стартовая</h1>'
    )

def index_3(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'users': users,
    }
    return render(
        request,
        'index.html',
        context
    )
def show_admin(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'show.html',
    )
def admin_show(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'admin.html',
        context={"users":User.objects.all()}
    )

