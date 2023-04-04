# Generated by Django 3.2 on 2023-04-03 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0077_alter_activity_topic_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='base.activity_template', verbose_name='قالب'),
        ),
        migrations.AlterField(
            model_name='activity_topic',
            name='template',
            field=models.ManyToManyField(blank=True, related_name='templates', to='base.Activity_Template', verbose_name='قالب ها'),
        ),
    ]