# Generated by Django 3.2 on 2023-04-04 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0085_rename_is_introduced_masir_group_introduced'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='support', to='base.user_detail', verbose_name='پشتیبان'),
        ),
    ]
