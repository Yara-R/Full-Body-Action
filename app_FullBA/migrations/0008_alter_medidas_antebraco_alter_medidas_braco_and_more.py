# Generated by Django 4.2 on 2023-05-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_FullBA', '0007_avaliacao_comentario_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidas',
            name='antebraco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='braco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='cintura',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='costas',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='coxa',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='ombro',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='panturrilha',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='peito',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='pescoco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='quadril',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
# Generated by Django 4.2 on 2023-05-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_FullBA', '0007_avaliacao_comentario_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidas',
            name='antebraco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='braco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='cintura',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='costas',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='coxa',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='ombro',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='panturrilha',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='peito',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='pescoco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='quadril',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
