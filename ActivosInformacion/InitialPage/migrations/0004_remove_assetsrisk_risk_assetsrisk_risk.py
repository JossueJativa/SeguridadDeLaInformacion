# Generated by Django 5.0 on 2024-01-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InitialPage', '0003_remove_assetsrisk_risk_assetsrisk_risk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetsrisk',
            name='Risk',
        ),
        migrations.AddField(
            model_name='assetsrisk',
            name='risk',
            field=models.ManyToManyField(to='InitialPage.risk'),
        ),
    ]
