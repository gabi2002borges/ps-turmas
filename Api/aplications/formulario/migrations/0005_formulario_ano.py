# Generated by Django 4.0 on 2021-12-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0004_remove_formulario_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='ano',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]