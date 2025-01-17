# Generated by Django 5.1.2 on 2025-01-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Genre', models.CharField(choices=[('F', 'Fantasy'), ('R', 'Romance'), ('D', 'Drama'), ('C', 'Comedy'), ('H', 'Horror'), ('A', 'Action'), ('M', 'Musical'), ('T', 'Thriller'), ('D', 'Documentary'), ('SF', 'ScienceFiction'), ('AM', 'Animation'), ('AD', 'Adventure')], max_length=2)),
            ],
        ),
    ]