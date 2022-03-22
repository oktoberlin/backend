# Generated by Django 3.2.11 on 2022-03-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_datasupir'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasupir',
            options={'verbose_name': 'Data Supir', 'verbose_name_plural': 'Data Supir'},
        ),
        migrations.AlterModelOptions(
            name='mobileuser',
            options={'verbose_name': 'Data Karyawan', 'verbose_name_plural': 'Data Karyawan'},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['editedTime'], 'verbose_name': 'Data BON Supir', 'verbose_name_plural': 'Data BON Supir'},
        ),
        migrations.AlterField(
            model_name='note',
            name='idSupir',
            field=models.CharField(default='', max_length=100, verbose_name='ID Supir'),
        ),
    ]