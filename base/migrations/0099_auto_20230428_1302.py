# Generated by Django 3.2 on 2023-04-28 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0098_auto_20230427_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': 'رای', 'verbose_name_plural': 'آرای نظرسنجی مردمی'},
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='vote',
            new_name='selections',
        ),
    ]
