from django.db import models
from django.db.models import TextChoices


class Position(TextChoices):
    TRAINEE = 'TR', 'Trainee'
    JUNIOR = 'JR', 'Junior'
    SENIOR = 'SR', 'Senior'
    CEO = 'CEO', 'CEO'


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
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

    def __str__(self):
        return self.name
