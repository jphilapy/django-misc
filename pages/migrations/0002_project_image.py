# Generated by Django 4.2.13 on 2024-06-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image",
            field=models.ImageField(null=True, upload_to="uploads/images"),
        ),
    ]
