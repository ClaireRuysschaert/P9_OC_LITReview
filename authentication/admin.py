from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import LITUserCreationForm
from .models import LITUser


class CustomUserAdmin(UserAdmin):
	add_form = LITUserCreationForm
	form = LITUserCreationForm
	model = LITUser
	list_display = ["email", "username", "is_staff",]
	fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("follows",)}),)
	add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("follows",)}),)

admin.site.register(LITUser, CustomUserAdmin)
