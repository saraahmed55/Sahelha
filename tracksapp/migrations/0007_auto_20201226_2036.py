# Generated by Django 3.1.4 on 2020-12-26 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0006_auto_20201226_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracksapp',
            old_name='trackpath',
            new_name='trackpathname',
        ),
    ]
