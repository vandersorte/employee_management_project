# Generated by Django 4.2.16 on 2024-12-15 21:05

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('nascimento', models.DateField(verbose_name='Nascimento')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=100, verbose_name='Gênero')),
                ('cpf', models.CharField(default='', max_length=14, verbose_name='CPF')),
                ('cargo', models.CharField(choices=[('Estágio', 'Estágiário'), ('Jr', 'Junior'), ('Pl', 'Pleno'), ('Sr', 'Senior'), ('Tl', 'Tech Lead')], max_length=100, verbose_name='Cargo')),
                ('remuneracao', models.CharField(default='', max_length=100, validators=[core.models.Funcionarios.validate_number], verbose_name='Remuneração')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
