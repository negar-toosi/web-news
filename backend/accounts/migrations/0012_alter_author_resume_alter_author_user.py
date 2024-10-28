# Generated by Django 4.2 on 2024-10-27 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_alter_author_biography"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="resume",
            field=models.FileField(blank=True, null=True, upload_to="resumes/"),
        ),
        migrations.AlterField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
