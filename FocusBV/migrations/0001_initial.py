# Generated by Django 3.2.1 on 2021-09-21 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccidenteVehicular',
            fields=[
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
                ('claseAC', models.CharField(choices=[('A', 'Automovil'), ('B', 'Omnibus'), ('C', 'Camion'), ('D', 'Motocicleta'), ('E', 'Atropellado')], default=None, max_length=10)),
                ('cantVehiculos', models.CharField(blank=True, max_length=200)),
                ('cantPersonas', models.IntegerField()),
                ('corteTransito', models.BooleanField()),
                ('tipoCalle', models.CharField(choices=[('C', 'Calle'), ('A', 'Avenida'), ('R', 'Ruta'), ('U', 'Undefined')], default='U', max_length=10)),
                ('herido', models.CharField(max_length=20)),
                ('servEmergencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Accidente Vehicular',
                'verbose_name_plural': 'Accidentes Vehiculares',
            },
        ),
        migrations.CreateModel(
            name='EscapeGas',
            fields=[
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
                ('tipoIncidente', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Escape de Gas',
                'verbose_name_plural': 'Escapes de Gas',
            },
        ),
        migrations.CreateModel(
            name='FormularioAuxiliar',
            fields=[
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
                ('aux', models.TextField(default='Formulario Auxiliar')),
            ],
            options={
                'verbose_name': 'Formulario Auxiliar',
                'verbose_name_plural': 'Formularios Auxiliares',
            },
        ),
        migrations.CreateModel(
            name='IncendioBaldio',
            fields=[
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
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
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
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
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
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
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
                ('tipoVehiculo', models.CharField(max_length=20)),
                ('humoLlamas', models.CharField(max_length=30)),
                ('vehiculoOcup', models.BooleanField()),
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
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
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
            name='PerdidaCombustible',
            fields=[
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
                ('tipoCombustible', models.CharField(max_length=20)),
                ('servEmergencia', models.CharField(max_length=30)),
                ('hayVictimas', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Perdida de Combustible',
                'verbose_name_plural': 'Perdidas de Combustible',
            },
        ),
        migrations.CreateModel(
            name='RescateAnimal',
            fields=[
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
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
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
                ('esPolicia', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Rescate de Cadaver',
                'verbose_name_plural': 'Rescates de Cadaveres',
            },
        ),
        migrations.CreateModel(
            name='RescatePersonaVia',
            fields=[
                ('idAlarma', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('hora', models.TimeField()),
                ('receptor', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('referencia', models.TextField(max_length=100, null=True)),
                ('estadoPersona', models.CharField(max_length=30)),
                ('lesion', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Rescate de Persona en Via Publica',
                'verbose_name_plural': 'Rescates de Personas en Via Publica',
            },
        ),
    ]
