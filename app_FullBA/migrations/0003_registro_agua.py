# Generated by Django 5.0.dev20230402075433 on 2023-04-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_FullBA', '0002_remove_usuario_idade_usuario_email_usuario_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Agua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.DateTimeField()),
                ('quantidade_ml', models.IntegerField()),
            ],
        ),
    ]