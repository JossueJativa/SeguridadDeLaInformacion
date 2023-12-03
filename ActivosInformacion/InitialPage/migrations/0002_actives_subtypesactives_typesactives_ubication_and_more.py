# Generated by Django 4.2.4 on 2023-12-03 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InitialPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
                ('quantity', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='SubtypesActives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TypesActives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ubication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='programissue',
            name='issueSource',
        ),
        migrations.RemoveField(
            model_name='programissue',
            name='statusIssue',
        ),
        migrations.RemoveField(
            model_name='programissue',
            name='typeIssue',
        ),
        migrations.RemoveField(
            model_name='scopes',
            name='statusScope',
        ),
        migrations.DeleteModel(
            name='Goals',
        ),
        migrations.DeleteModel(
            name='IssueSource',
        ),
        migrations.DeleteModel(
            name='ProgramIssue',
        ),
        migrations.DeleteModel(
            name='Scopes',
        ),
        migrations.DeleteModel(
            name='StatusIssue',
        ),
        migrations.DeleteModel(
            name='TypeIssueSource',
        ),
        migrations.AddField(
            model_name='subtypesactives',
            name='typeActive',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InitialPage.typesactives'),
        ),
        migrations.AddField(
            model_name='actives',
            name='typeActive',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InitialPage.typesactives'),
        ),
        migrations.AddField(
            model_name='actives',
            name='ubication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InitialPage.ubication'),
        ),
    ]
