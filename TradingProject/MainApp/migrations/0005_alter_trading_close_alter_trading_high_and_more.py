# Generated by Django 4.1.7 on 2023-02-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_delete_csvfileuplaod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trading',
            name='CLOSE',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trading',
            name='HIGH',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trading',
            name='LOW',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trading',
            name='OPEN',
            field=models.CharField(max_length=50),
        ),
    ]
