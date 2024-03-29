# Generated by Django 4.2.2 on 2023-07-05 12:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogapp", "0008_alter_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="blogpost", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
