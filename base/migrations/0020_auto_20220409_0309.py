# Generated by Django 3.2 on 2022-04-08 22:39

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_club_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='club_file',
            name='date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ'),
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='مقدار')),
                ('date', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charities', to='base.user_detail', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'فایل\u200c',
                'verbose_name_plural': 'فایل\u200cهای باشگاه',
            },
        ),
    ]
