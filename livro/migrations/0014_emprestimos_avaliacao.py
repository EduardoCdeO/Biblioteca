# Generated by Django 4.2.7 on 2023-11-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0013_remove_emprestimos_tempo_duracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
