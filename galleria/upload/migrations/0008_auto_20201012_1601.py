# Generated by Django 3.1.1 on 2020-10-12 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20201012_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo_name',
            new_name='name',
        ),
    ]
