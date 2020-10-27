from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from users import models
from .models import Post, Comment, Tag, Message

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email','username']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1','password2')
        }),
    )

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['userpro', 'created_on']

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
admin.site.register(models.Message)
