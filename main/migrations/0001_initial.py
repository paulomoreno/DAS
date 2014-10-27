# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, name=b'id')),
                ('data_hora', models.DateTimeField()),
                ('checkin', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(to='main.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('cnpj', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('razao_social', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Especializacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.PositiveSmallIntegerField()),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crm', models.CharField(max_length=16)),
                ('duracao_consulta', models.PositiveSmallIntegerField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'endere\xc3\xa7o de email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('rg', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=60)),
                ('sobrenome', models.CharField(max_length=60)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.OneToOneField(null=True, to='main.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='horario',
            name='medico',
            field=models.ForeignKey(to='main.Medico'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(to='main.Medico'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(null=True, to='main.Usuario'),
            preserve_default=True,
        ),
    ]
