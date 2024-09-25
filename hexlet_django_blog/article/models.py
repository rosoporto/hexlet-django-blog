from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    TRAINEE = 'TR'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    CEO = 'CEO'
    CHOICES_PERSONE = [
        (TRAINEE, 'Trainee'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (CEO, 'CEO')
    ]
    name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=3,
        choices=CHOICES_PERSONE,
        default=TRAINEE,
    )

    def __str__(self):
        return self.name
