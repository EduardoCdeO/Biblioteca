# Generated by Django 4.2.7 on 2023-11-07 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_ativo'),
        ('livro', '0010_emprestimos_nome_emprestado_anonimo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='nome_emprestado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]
