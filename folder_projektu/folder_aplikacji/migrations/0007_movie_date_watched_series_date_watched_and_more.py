# Generated by Django 5.1.2 on 2025-01-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0006_rename_episodes_s_series_episodes_watched_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Date_watched',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1),
        ),
        migrations.AddField(
            model_name='series',
            name='Date_watched',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Review',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='series',
            name='Review',
            field=models.CharField(blank=True, max_length=20000),
        ),
    ]
