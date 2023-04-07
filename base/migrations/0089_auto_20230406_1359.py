# Generated by Django 3.2 on 2023-04-06 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0088_auto_20230405_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_topic',
            name='level1',
        ),
        migrations.RemoveField(
            model_name='activity_topic',
            name='level2',
        ),
        migrations.RemoveField(
            model_name='activity_topic',
            name='level3',
        ),
        migrations.AddField(
            model_name='activity_template',
            name='info',
            field=models.TextField(blank=True, default='', null=True, verbose_name='شرح'),
        ),
        migrations.AddField(
            model_name='masir_group',
            name='unlocked',
            field=models.ManyToManyField(blank=True, related_name='unlocked', to='base.Activity_Template', verbose_name='فعالیت های باز شده'),
        ),
    ]