from django.db import models
from django.contrib.auth import get_user_model
from hexlet_django_blog.category.models import Category


class Position(models.TextChoices):
    TRAINEE = 'TR', 'Trainee'
    JUNIOR = 'JR', 'Junior'
    SENIOR = 'SR', 'Senior'
    CEO = 'CEO', 'CEO'


class ArticleStatus(models.TextChoices):
    DRAFT = 'DR', 'Draft'
    PUBLISHED = 'PB', 'Published'


class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='articles'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=2,
        choices=ArticleStatus.choices,
        default=ArticleStatus.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']


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
