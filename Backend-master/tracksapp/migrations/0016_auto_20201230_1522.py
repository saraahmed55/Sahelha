# Generated by Django 3.1.4 on 2020-12-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0015_auto_20201230_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracksapp',
            name='courses',
        ),
        migrations.AddField(
            model_name='tracksapp',
            name='courses',
            field=models.ManyToManyField(to='tracksapp.courses'),
        ),
    ]
