# Generated by Django 3.2 on 2023-04-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0096_activity_cheated'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='score6',
            field=models.IntegerField(default=0, verbose_name='معیار 6'),
        ),
        migrations.AddField(
            model_name='activity',
            name='score7',
            field=models.IntegerField(default=0, verbose_name='معیار 7'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score1',
            field=models.IntegerField(default=0, verbose_name='معیار 1'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score2',
            field=models.IntegerField(default=0, verbose_name='معیار 2'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score3',
            field=models.IntegerField(default=0, verbose_name='معیار 3'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score4',
            field=models.IntegerField(default=0, verbose_name='معیار 4'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score5',
            field=models.IntegerField(default=0, verbose_name='معیار 5'),
        ),
    ]