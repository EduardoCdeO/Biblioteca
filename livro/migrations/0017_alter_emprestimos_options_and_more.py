# Generated by Django 4.2.7 on 2023-11-21 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0016_alter_emprestimos_avaliacao_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimos',
            options={'verbose_name': 'Empréstimo'},
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 13, 47, 59, 374819)),
        ),
    ]
