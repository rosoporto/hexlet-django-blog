from django.db import models
from django.db.models import TextChoices
from hexlet_django_blog.category.models import Category


class Position(TextChoices):
    TRAINEE = 'TR', 'Trainee'
    JUNIOR = 'JR', 'Junior'
    SENIOR = 'SR', 'Senior'
    CEO = 'CEO', 'CEO'


class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=3,
        choices=Position.choices,
        default=Position.TRAINEE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
