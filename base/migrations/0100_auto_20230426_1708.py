# Generated by Django 3.2 on 2023-04-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0099_auto_20230425_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='is_valid',
        ),
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
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='تایید شده'),
        ),
        migrations.AddField(
            model_name='vote',
            name='is_voted',
            field=models.BooleanField(default=False, verbose_name='رای داده'),
        ),
        migrations.AddField(
            model_name='vote',
            name='vote',
            field=models.ManyToManyField(blank=True, related_name='vote', to='base.Top_Work', verbose_name='رای ها'),
        ),
    ]
