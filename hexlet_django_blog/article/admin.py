from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article, Employee


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ['name', 'body']
    list_filter = (('created_at', DateFieldListFilter),)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at', 'updated_at')
    search_fields = ['name', 'position']
    list_filter = (('created_at', DateFieldListFilter),)
