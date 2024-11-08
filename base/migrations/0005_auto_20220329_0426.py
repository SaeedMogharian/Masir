# Generated by Django 3.2 on 2022-03-28 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220329_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='نامشخص', max_length=50, verbose_name='نام مدرسه')),
            ],
            options={
                'verbose_name': 'مدرسه',
                'verbose_name_plural': 'مدارس',
            },
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='school',
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='accessibility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='base.accessibility', verbose_name='دسترسی'),
        ),
    ]
