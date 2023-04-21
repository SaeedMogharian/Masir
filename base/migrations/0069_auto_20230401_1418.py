# Generated by Django 3.2 on 2023-04-01 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0068_activity_topic_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_topic',
            name='main',
            field=models.BooleanField(default=False, verbose_name='فعالیت اصلی؟'),
        ),
        migrations.AlterField(
            model_name='activity_topic',
            name='manzel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_topics', to='base.manzel', verbose_name='منزل'),
        ),
    ]
