# Generated by Django 3.1.6 on 2021-02-15 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0020_auto_20201230_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracksapp',
            old_name='image_in_detail',
            new_name='background_in_detail',
        ),
    ]
