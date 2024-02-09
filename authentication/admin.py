from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import LITUserChangeForm, LITUserCreationForm
from .models import LITUser


class CustomUserAdmin(UserAdmin):
    add_form = LITUserCreationForm
    form = LITUserChangeForm
    model = LITUser  # type: ignore[assignment]
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("follows",)}),)  # type: ignore[operator]
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("follows",)}),)


admin.site.register(LITUser, CustomUserAdmin)
