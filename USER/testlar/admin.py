from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model=CustomUser
    fieldsets=((None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),('Personal', {'fields': ('portfolio','age'),}),)

    list_display = ['email', 'username', 'portfolio', 'is_staff', ]

admin.site.register(CustomUser,CustomUserAdmin)
