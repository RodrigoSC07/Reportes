# Generated by Django 4.2.7 on 2023-12-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enfermeros', '0003_enfermero_dato'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfermero',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True),
        ),
    ]
