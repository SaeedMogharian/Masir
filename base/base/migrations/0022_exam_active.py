# Generated by Django 3.2 on 2022-04-08 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20220409_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='active',
            field=models.BooleanField(default=False, verbose_name='فعال'),
        ),
    ]
