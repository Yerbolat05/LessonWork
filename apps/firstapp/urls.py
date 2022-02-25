from django.urls import (
    path, re_path
)
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path(
        '',
        views.admin_show,
        name = 'page_main'),
    re_path(
        r'^show/(?P<username>\w+)/$',
        views.show_admin,
        name = 'page_show'),
    path(
        'delete/',
        views.delete,
        name = 'page_delete'
    )
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

