# Generated by Django 5.1.1 on 2024-10-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="state",
            field=models.CharField(
                choices=[("draft", "draft"), ("published", "published")],
                default="draft",
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
