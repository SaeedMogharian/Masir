# Generated by Django 3.2 on 2023-04-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0086_message_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='club_file',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ'),
        ),
    ]
