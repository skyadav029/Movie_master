# Generated by Django 4.1 on 2023-11-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_save_movie_ids_save_movie_name_save_movie_usr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save_movie',
            name='ids',
            field=models.IntegerField(default=0),
        ),
    ]
