# Generated by Django 4.2.2 on 2023-07-01 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0002_post_title_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_date",
            field=models.DateField(
                auto_created=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
