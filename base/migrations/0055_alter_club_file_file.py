# Generated by Django 3.2 on 2022-04-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_auto_20220413_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='base/static/club/', verbose_name='فایل'),
        ),
    ]
