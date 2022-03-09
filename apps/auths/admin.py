from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auths.forms import (
    CustomUserCreationForm,
    CustomUserChangeFrom,
)
from auths.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeFrom
    model = CustomUser
    list_display = ('email', 'is_active',)
    list_filter = ('email', 'is_active',)
    
    fieldsets = (
        (
            None, {
                'fields': (
                    'email', 'password',
                ),
            }
        ),
        (
            'Permissions', {
                'fields': ('is_active',)
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'password1', 'password2', 'is_active',
                ),
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(
    CustomUser, CustomUserAdmin
)# Register your models here.
