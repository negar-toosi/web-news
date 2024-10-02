# Generated by Django 4.2 on 2024-10-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_news_created_date_alter_news_pub_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=225)),
                ("last_name", models.CharField(max_length=225)),
            ],
        ),
    ]
