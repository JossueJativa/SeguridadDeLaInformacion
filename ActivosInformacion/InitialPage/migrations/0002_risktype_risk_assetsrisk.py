# Generated by Django 5.0 on 2024-01-20 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InitialPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dimention', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InitialPage.risktype')),
            ],
        ),
        migrations.CreateModel(
            name='AssetsRisk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimention', models.CharField(max_length=255, null=True)),
                ('asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InitialPage.assets')),
                ('risk', models.ManyToManyField(to='InitialPage.risk')),
                ('risktype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InitialPage.risktype')),
            ],
        ),
    ]