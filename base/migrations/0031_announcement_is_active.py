# Generated by Django 3.2 on 2022-04-11 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_rename_is_active_announcement_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
    ]
