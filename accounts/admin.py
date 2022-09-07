from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.add_fieldsets[0][1]['fields'] = ('username', 'password1', 'password2', 'email', 'profile_image',)

admin.site.register(User, UserAdmin)
