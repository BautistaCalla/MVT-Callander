# Generated by Django 4.0.5 on 2022-06-14 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiPrimerProyectoApp', '0003_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
