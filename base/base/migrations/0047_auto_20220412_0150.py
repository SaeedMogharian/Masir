# Generated by Django 3.2 on 2022-04-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_auto_20220412_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='score',
        ),
        migrations.AddField(
            model_name='activity',
            name='score1',
            field=models.IntegerField(default=0, verbose_name='امتیاز محتوای مناسب، غنی و منسجم'),
        ),
        migrations.AddField(
            model_name='activity',
            name='score2',
            field=models.IntegerField(default=0, verbose_name='امتیاز تناسب قالب و محتوای انتخابی'),
        ),
        migrations.AddField(
            model_name='activity',
            name='score3',
            field=models.IntegerField(default=0, verbose_name='امتیاز رعایت نکات حداقلی فنی درباره\u200cی هر قالب'),
        ),
        migrations.AddField(
            model_name='activity',
            name='score4',
            field=models.IntegerField(default=0, verbose_name='امیتیاز خلاقیت و نوآوری'),
        ),
        migrations.AddField(
            model_name='activity',
            name='score5',
            field=models.IntegerField(default=0, verbose_name='امتیاز جذابیت برای مخاطب'),
        ),
        migrations.AddField(
            model_name='activity',
            name='score6',
            field=models.IntegerField(default=0, verbose_name='امتیاز اشاره به کاربردی بودن مفاهیم در زندگی امروزی، به صورت مستقیم یا غیرمستقیم'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='state',
            field=models.CharField(choices=[('1', 'ارسال شده'), ('2', 'در حال داوری'), ('3', 'داوری شده'), ('4', 'اعلام شده')], default='1', max_length=1, verbose_name='وضعیت'),
        ),
    ]
