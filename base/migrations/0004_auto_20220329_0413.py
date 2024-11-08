# Generated by Django 3.2 on 2022-03-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220328_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='نامشخص', max_length=20, verbose_name='استان')),
                ('name', models.CharField(default='نامشخص', max_length=50, verbose_name='نام شهر')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهرها',
            },
        ),
        migrations.AddField(
            model_name='user_detail',
            name='nationalcode',
            field=models.CharField(default='xxxxxxxxxx', max_length=10, verbose_name='کد ملی'),
        ),
    ]
