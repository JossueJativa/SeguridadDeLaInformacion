# Generated by Django 4.2.7 on 2023-12-10 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InitialPage', '0009_assetsvalue_subtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetsvalue',
            name='subtype',
        ),
    ]
