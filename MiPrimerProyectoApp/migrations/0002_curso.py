# Generated by Django 4.0.5 on 2022-06-13 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiPrimerProyectoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('comision', models.CharField(max_length=30)),
            ],
        ),
    ]
