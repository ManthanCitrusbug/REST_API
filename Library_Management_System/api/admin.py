from django.contrib import admin
from .models import Company
from django.contrib.auth.models import User
# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']