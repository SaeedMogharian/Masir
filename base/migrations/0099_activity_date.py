# Generated by Django 3.2 on 2023-04-10 19:31

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0098_club_file_referee'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ'),
        ),
    ]
