# Generated by Django 3.1.1 on 2020-10-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0015_auto_20201014_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='uploaded',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
