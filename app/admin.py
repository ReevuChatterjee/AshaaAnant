from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


admin.site.register(models.RescueDB)


class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = ("email", "username", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(models.CustomUser, CustomUserAdmin)
# Register your models here.
