from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path(settings.ADMIN_SITE_URLS, admin.site.urls),
    path('', include('firstapp.urls')),
    #path("",index),
]+ static(
    settings.STATIC_URL,
    document_root = settings.STATIC_ROOT
)
if settings.DEBUG: 
    urlpatterns += [
        path('__debug__/',include('debug_toolbar.urls')),
    ]
