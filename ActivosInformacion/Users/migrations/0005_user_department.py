# Generated by Django 4.2.7 on 2023-12-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_rename_identity_user_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
