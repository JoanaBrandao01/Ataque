# Generated by Django 4.2.5 on 2023-09-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_sedimentacao_tempo_sedimentacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sedimentacao',
            name='capacidade',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sedimentacao',
            name='etapa',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sedimentacao',
            name='nivel_tanque',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sedimentacao',
            name='processo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sedimentacao',
            name='tempo_estimado',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sedimentacao',
            name='viscosidade',
            field=models.CharField(max_length=255),
        ),
    ]