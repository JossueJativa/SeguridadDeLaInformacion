# Generated by Django 5.0 on 2024-01-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InitialPage', '0002_risktype_risk_assetsrisk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetsrisk',
            name='risk',
        ),
        migrations.AddField(
            model_name='assetsrisk',
            name='Risk',
            field=models.ManyToManyField(to='InitialPage.risk'),
        ),
    ]