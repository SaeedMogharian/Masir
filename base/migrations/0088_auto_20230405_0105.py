# Generated by Django 3.2 on 2023-04-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0087_auto_20230405_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='score6',
        ),
        migrations.AlterField(
            model_name='activity',
            name='score2',
            field=models.IntegerField(default=0, verbose_name='امتیاز رعایت نکات حداقلی فنی درباره\u200cی هر قالب'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score3',
            field=models.IntegerField(default=0, verbose_name='امیتیاز خلاقیت و نوآوری'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score4',
            field=models.IntegerField(default=0, verbose_name='امتیاز جذابیت برای مخاطب'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score5',
            field=models.IntegerField(default=0, verbose_name='امتیاز اشاره به کاربردی بودن مفاهیم در زندگی امروزی، به صورت مستقیم یا غیرمستقیم'),
        ),
    ]
