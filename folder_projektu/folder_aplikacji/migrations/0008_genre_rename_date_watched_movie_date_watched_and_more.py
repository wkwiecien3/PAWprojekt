# Generated by Django 5.1.2 on 2025-01-20 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0007_movie_date_watched_series_date_watched_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Date_watched',
            new_name='date_watched',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='Date_watched',
            new_name='date_watched',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='Episodes_watched',
            new_name='episodes_watched',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='Rating',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Review',
        ),
        migrations.RemoveField(
            model_name='series',
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='series',
            name='Review',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='folder_aplikacji.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='series',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='folder_aplikacji.genre'),
        ),
        migrations.AddField(
            model_name='series',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
