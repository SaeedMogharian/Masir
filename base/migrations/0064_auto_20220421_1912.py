# Generated by Django 3.2 on 2022-04-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0063_alter_masir_group_and_achivement_rel_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='file',
        ),
        migrations.RemoveField(
            model_name='club_file',
            name='file',
        ),
        migrations.AddField(
            model_name='activity',
            name='comment',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='توضیحات داور'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='state',
            field=models.CharField(choices=[('1', 'ارسال شده'), ('2', 'در حال داوری'), ('3', 'داوری شده'), ('4', 'اعلام شده'), ('5', 'رد شده')], default='1', max_length=1, verbose_name='وضعیت'),
        ),
    ]
