# Generated by Django 5.2.1 on 2025-05-16 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogador',
            options={'ordering': ['-jogos_jogados'], 'verbose_name': 'Jogador', 'verbose_name_plural': 'Jogadores'},
        ),
    ]
