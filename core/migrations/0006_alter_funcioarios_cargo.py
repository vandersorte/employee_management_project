# Generated by Django 4.2.16 on 2024-11-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_funcioarios_naturalidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcioarios',
            name='cargo',
            field=models.CharField(choices=[('Estágio', 'Estágiário'), ('Jr', 'Junior'), ('Pl', 'Pleno'), ('Sr', 'Senior'), ('Tl', 'Tech Lead')], default=' ', max_length=100, verbose_name='Cargo'),
        ),
    ]
