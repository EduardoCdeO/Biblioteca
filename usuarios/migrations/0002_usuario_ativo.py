# Generated by Django 4.2.7 on 2023-11-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]