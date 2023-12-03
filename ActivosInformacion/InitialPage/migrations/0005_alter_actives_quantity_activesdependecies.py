# Generated by Django 4.2.7 on 2023-12-03 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InitialPage', '0004_remove_typesactives_subtypeactive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actives',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='ActivesDependecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subactiveDependent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DependentSubtypeActive', to='InitialPage.subtypesactives')),
                ('subactiveIndependent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='IndependentSubtypeActive', to='InitialPage.subtypesactives')),
                ('typeActiveDependen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DependentTypeActive', to='InitialPage.typesactives')),
                ('typeActiveIndependent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='IndependentTypeActive', to='InitialPage.typesactives')),
            ],
        ),
    ]
