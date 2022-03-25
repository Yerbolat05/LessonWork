from multiprocessing import context
from unittest import loader
from warnings import filters
from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from auths.forms import CustomUserForm
from django.views import View
from django.template import loader
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)


from auths.models import CustomUser

from .models import (
    Account,
    Homework,
    File,
    Student,
)

class IndexView(View):

    queryset: QuerySet = \
        Homework.objects.get_not_deleted()
    
    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs : dict
    ): 
        if not request.user.is_authenticated:
            return render(
                request,
                'firstapp/index.html'
            )
        homeworks : QuerySet = self.queryset.filter(
            user = request.user
        )
        if not homeworks:
            homeworks = Homework.objects.all()

        context: dict = {
            'ctx_title' : 'Главная страница',
            'ctx_homeworks' : homeworks,
        }

        template_name = loader.get_template(
            'firstapp/index.html'
            )

        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type = 'text/html'
        )


def index_2(request: WSGIRequest) -> HttpResponse:
    """Start Page"""
    return HttpResponse(
        '<h1>Страница : Стартовая</h1>'
    )


def index_3(request: WSGIRequest) -> HttpResponse:

    users: QuerySet = CustomUser.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'users': users,
    }
    return render(
        request,
        'firstapp/index.html',
        context
    )


def show_admin(request: WSGIRequest, user_id : int) -> HttpResponse:
    user: CustomUser = CustomUser.objects.get(
        id = user_id
    )
    context: dict = {
        'ctx_user' : user,
    }
    return render(
        request,
        'firstapp/show.html',
        context
    )


def admin_show(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'firstapp/admin.html',
        context={"users": CustomUser.objects.all()}
    )


def delete(request: WSGIRequest, username : str) -> HttpResponse:
    user: CustomUser = CustomUser.objects.get(
        user_id = user_id
    )
    return render(
        request,
    )


class RegisterView(View):
    def get(
        self,
        request : HttpResponse,
        *args: tuple,
        **kwargs : dict):
        form: CustomUserForm = CustomUserForm()
        return render(
            request,
            'firstapp/register.html',
            context={"form": form}
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict):
        form: CustomUserForm = CustomUserForm(
            request.POST
        )
        if form.is_valid():
            user: CustomUser = form.save(
                commit=False
            )
            email: str = form.cleaned_data['email']
            password: str = form.cleaned_data['password']
            user.email = email
            user.set_password(password)
            user.save()

            user: CustomUser = dj_authenticate(
                email=email,
                password=password
            )
            if user and user.is_active:
                breakpoint()
                dj_login(request, user)

                homeworks: QuerySet = Homework.objects.filter(
                    user=request.user
                )
                return render(
                    request,
                    'firstapp/index.html',
                    {'homeworks': homeworks}
                )
        context: dict = {
        'form': form
        }
        return render(
            request,
            'firstapp/register.html',
            context
        )


def register(request: WSGIRequest) -> HttpResponse:

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    if form.is_valid():
        user: CustomUser = form.save(
            commit=False
        )
        email: str = form.cleaned_data['email']
        password: str = form.cleaned_data['password']
        user.email = email
        user.set_password(password)
        user.save()

        user: CustomUser = dj_authenticate(
            email=email,
            password=password
        )
        if user and user.is_active:

            dj_login(request, user)

            homeworks: QuerySet = Homework.objects.filter(
                user=request.user
            )
            return render(
                request,
                'firstapp/index.html',
                {'homeworks': homeworks}
            )
    context: dict = {
        'form': form
    }
    return render(
        request,
        'firstapp/register.html',
        context
    )


class LoginView(View):

    def get(
        self,
        request : HttpResponse,
        *args: tuple,
        **kwargs : dict):
        return render(
            request,
            'firstapp/login.html'
        )

    def post(
        self,
        request : WSGIRequest,
        *args: tuple,
        **kwargs : dict
    ):
        template_name = loader.get_template(
            'firstapp/login.html'
        )

        email: str = request.POST['email']
        password: str = request.POST['password']

        user: CustomUser = dj_authenticate(
            email=email,
            password=password
        )

        if not user:
            return render(
                request,
                template_name,
                {'error_message': 'Неверные данные'}
            )
        if not user.is_active:
            return render(
                request,
                template_name,
                {'error_message': 'Ваш аккаунт был удален'}
            )
        dj_login(request, user)

        homeworks: QuerySet = Homework.objects.filter(
        user=request.user
        )
        context: dict = {
            'ctx_homeworks': homeworks
        }
        template_name = loader.get_template(
            'firstapp/index.html'
        )
        
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type = 'text/html'
        )

def logout(request: WSGIRequest) -> HttpResponse:

    dj_logout(request)

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    context: dict = {
        'form': form,
    }
    return render(
        request,
        'firstapp/login.html',
        context
    )
