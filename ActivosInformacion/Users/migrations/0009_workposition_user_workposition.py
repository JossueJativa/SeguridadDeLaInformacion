# Generated by Django 4.2.7 on 2023-12-03 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_alter_user_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='workPosition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.workposition'),
        ),
    ]