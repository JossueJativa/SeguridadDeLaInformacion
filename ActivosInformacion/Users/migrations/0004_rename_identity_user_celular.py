# Generated by Django 4.2.4 on 2023-12-08 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_rename_celular_user_identity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='identity',
            new_name='celular',
        ),
    ]