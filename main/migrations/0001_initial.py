# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_medico', models.BooleanField(default=False)),
                ('is_cliente', models.BooleanField(default=False)),
                ('is_secretaria', models.BooleanField(default=False)),
                ('rg', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('usuario_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=('main.usuario',),
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
                ('nome', models.CharField(unique=True, max_length=60)),
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
                ('usuario_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('crm', models.CharField(max_length=16)),
                ('duracao_consulta', models.PositiveSmallIntegerField(max_length=15)),
                ('especializacao', models.ForeignKey(to='main.Especializacao')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
            bases=('main.usuario',),
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('usuario_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Secretaria',
                'verbose_name_plural': 'Secretarias',
            },
            bases=('main.usuario',),
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
            name='convenio',
            field=models.ForeignKey(to='main.Convenio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
