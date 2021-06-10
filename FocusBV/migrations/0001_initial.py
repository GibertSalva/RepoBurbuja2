# Generated by Django 2.2 on 2021-06-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccidenteVehicular',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('sentido', models.CharField(max_length=15)),
                ('cantVehiculos', models.IntegerField()),
                ('cantPersonas', models.IntegerField()),
                ('herido', models.CharField(max_length=20)),
                ('corteTransito', models.BooleanField()),
                ('servEmergencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Accidente Vehicular',
                'verbose_name_plural': 'Accidentes Vehiculares',
            },
        ),
        migrations.CreateModel(
            name='IncendioBaldio',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('entreCalles', models.CharField(max_length=30)),
                ('riesgoProp', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Incendio de Baldio',
                'verbose_name_plural': 'Incendios de Baldios',
            },
        ),
        migrations.CreateModel(
            name='IncendioElectrico',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('desperfecto', models.CharField(max_length=30)),
                ('humoLlamas', models.CharField(max_length=30)),
                ('epec', models.CharField(max_length=30)),
                ('servEmergencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Incendio Electrico',
                'verbose_name_plural': 'Incendios Electricos',
            },
        ),
        migrations.CreateModel(
            name='IncendioForestal',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('sentido', models.CharField(max_length=15)),
                ('riesgoProp', models.BooleanField()),
                ('edificios', models.IntegerField()),
                ('servEmergencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Incendio Forestal',
                'verbose_name_plural': 'Incendios Forestales',
            },
        ),
        migrations.CreateModel(
            name='IncendioVehicular',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('tipoVehiculo', models.CharField(max_length=20)),
                ('humoLlamas', models.CharField(max_length=30)),
                ('localOcup', models.BooleanField()),
                ('gnc', models.CharField(max_length=20)),
                ('riesgoProp', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Incendio Vehicular',
                'verbose_name_plural': 'Incendios Vehiculares',
            },
        ),
        migrations.CreateModel(
            name='IncendioVivienda',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('entreCalles', models.CharField(max_length=30)),
                ('estadoFuego', models.CharField(max_length=30)),
                ('habitantes', models.CharField(max_length=20)),
                ('localHabit', models.CharField(max_length=40)),
                ('descVivienda', models.CharField(max_length=50)),
                ('espera', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Incendio de Vivienda',
                'verbose_name_plural': 'Incendios de Viviendas',
            },
        ),
        migrations.CreateModel(
            name='RescateAnimal',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('animal', models.CharField(max_length=15)),
                ('condicionAnimal', models.CharField(max_length=30)),
                ('vision', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Rescate Animal',
                'verbose_name_plural': 'Rescate de Animales',
            },
        ),
        migrations.CreateModel(
            name='RescateCadaver',
            fields=[
                ('idAlarma', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoSiniestro', models.CharField(max_length=30)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('esPolicia', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Rescate de Cadaver',
                'verbose_name_plural': 'Rescates de Cadaveres',
            },
        ),
    ]
