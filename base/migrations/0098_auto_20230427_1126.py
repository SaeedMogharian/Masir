# Generated by Django 3.2 on 2023-04-27 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0097_auto_20230420_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='masood_valid',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_image_1',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_image_2',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_image_3',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_image_4',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_image_5',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_music_1',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_music_2',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_music_3',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_music_4',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_music_5',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_video_1',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_video_2',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_video_3',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_video_4',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_video_5',
        ),
        migrations.AddField(
            model_name='vote',
            name='is_voted',
            field=models.BooleanField(default=False, verbose_name='رای داده'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='تایید شده'),
        ),
        migrations.CreateModel(
            name='Top_Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='شماره')),
                ('link', models.URLField(blank=True, null=True, verbose_name='لینک اثر')),
                ('type', models.CharField(choices=[('1', 'صوتی'), ('2', 'ویدیویی'), ('3', 'تصویری')], default='1', max_length=1, verbose_name='نوع اثر')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topworks', to='base.masir_group', verbose_name='گروه')),
            ],
            options={
                'verbose_name': 'عنوان اثر',
                'verbose_name_plural': 'آثار برتر',
            },
        ),
        migrations.AddField(
            model_name='vote',
            name='vote',
            field=models.ManyToManyField(blank=True, related_name='vote', to='base.Top_Work', verbose_name='رای ها'),
        ),
    ]