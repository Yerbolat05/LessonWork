from unicodedata import name
from django.urls import (
    path, re_path
)
from django.conf import settings
from django.conf.urls.static import static
from . import views
from firstapp.views import(
    IndexView,
)


urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name = 'page_main'
    ),
    # re_path(
    #     r'^show/(?P<username>\w+)/$',
    #     views.show_admin,
    #     name = 'page_show'),
    path(
        'show/<str:user_id>/',
        views.show_admin,
        name='page_show',
    ),
    path(
        'delete/',
        views.delete,
        name = 'page_delete'
    ),
    path(
        'register/',
        views.register,
        name = 'page_register'
    ),
    path(
        'login/',
        views.login,
        name = 'page_login'
    ),
    path(
        'logout/',
        views.logout,
        name = 'page_logout'
    )
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

