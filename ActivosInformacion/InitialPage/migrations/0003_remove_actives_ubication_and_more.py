# Generated by Django 4.2.7 on 2023-12-03 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InitialPage', '0002_actives_subtypesactives_typesactives_ubication_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actives',
            name='ubication',
        ),
        migrations.RemoveField(
            model_name='subtypesactives',
            name='typeActive',
        ),
        migrations.AddField(
            model_name='typesactives',
            name='subtypeActive',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InitialPage.subtypesactives'),
        ),
        migrations.DeleteModel(
            name='Ubication',
        ),
    ]
