# Generated by Django 5.1.3 on 2024-11-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_funcioarios_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcioarios',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='', max_length=100, verbose_name='Gênero'),
        ),
    ]
