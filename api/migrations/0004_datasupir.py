# Generated by Django 3.2.11 on 2022-03-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220318_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSupir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idSup', models.TextField()),
                ('namaSupir', models.TextField()),
                ('passSupir', models.TextField()),
                ('jenis', models.TextField()),
                ('noPol', models.TextField()),
            ],
        ),
    ]