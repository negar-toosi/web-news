# Generated by Django 4.2 on 2024-10-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0005_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="news/", verbose_name="image"),
        ),
    ]