# Generated by Django 4.2 on 2023-05-29 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_FullBA', '0015_rename_comentario_comentario_antebraco_rosca_inversa_punho_dumbell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario_antebraco_rosca_punho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('texto', models.TextField()),
            ],
        ),
    ]
