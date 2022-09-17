# Generated by Django 4.1.1 on 2022-09-16 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaAPI', '0005_alter_paciente_latitud_alter_paciente_longitud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='id_paciente',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='persona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinicaAPI.persona'),
        ),
    ]
