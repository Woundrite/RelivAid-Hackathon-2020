# Generated by Django 3.1.2 on 2020-10-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickermodel',
            name='ishelper',
            field=models.BooleanField(default=0),
        ),
    ]
