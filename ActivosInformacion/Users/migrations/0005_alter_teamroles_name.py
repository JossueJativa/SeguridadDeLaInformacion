# Generated by Django 4.2.4 on 2023-12-03 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_remove_user_workload_alter_teamroles_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamroles',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
