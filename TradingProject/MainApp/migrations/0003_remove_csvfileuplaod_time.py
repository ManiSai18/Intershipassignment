# Generated by Django 4.1.7 on 2023-02-21 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_csvfileuplaod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfileuplaod',
            name='time',
        ),
    ]
