# Generated by Django 3.2 on 2023-04-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0078_auto_20230403_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_topic',
            name='co_title',
            field=models.CharField(default='عنوان پیش\u200cفرض', max_length=100, verbose_name='عنوان معرفتی'),
        ),
    ]
