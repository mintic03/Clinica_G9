# Generated by Django 4.1.1 on 2022-09-20 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaAPI', '0010_alter_paciente_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='persona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinicaAPI.persona'),
        ),
    ]