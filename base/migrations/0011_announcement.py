# Generated by Django 3.2 on 2022-03-31 02:54

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_delete_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='متن پیش\u200cفرض', max_length=1000, verbose_name='متن اعلان')),
                ('date', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ')),
                ('is_active', models.BooleanField(default=True, verbose_name='نمایش در تابلوی اعلانات')),
            ],
            options={
                'verbose_name': 'اعلان',
                'verbose_name_plural': 'اعلانات',
            },
        ),
    ]
