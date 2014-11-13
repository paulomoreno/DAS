# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django_extensions.db.fields import UUIDField

#Nosso usuario base
class Usuario(AbstractUser):    
    #Tipo do usuario
    is_admin = models.BooleanField(default=False)
    is_medico = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)
    is_secretaria = models.BooleanField(default=False)

    #Informacoes comuns
    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15, unique=True)

    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=120)

    def __unicode__(self):
        return self.username + ' - ' + self.email
    
    def get_full_name(self):
        return self.first_name+" "+self.last_name

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Cliente(Usuario):
    #usuario = models.OneToOneField(Usuario, null=True)
    convenio = models.ForeignKey('Convenio')
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __unicode__(self):
        return self.first_name

class Secretaria(Usuario):
    #usuario = models.OneToOneField(Usuario, null=True)
    
    class Meta:
        verbose_name = "Secretaria"
        verbose_name_plural = "Secretarias"

class Medico(Usuario):
    #usuario = models.OneToOneField(Usuario, null=True)
    crm = models.CharField(max_length=16, unique=True)
    duracao_consulta = models.PositiveSmallIntegerField(max_length=15)
    especializacao = models.ForeignKey('Especializacao')

    def json(self):
        medico = {}
        medico['id'] = self.id
        medico['nome'] = self.first_name
        medico['sobrenome'] = self.last_name
        medico['email'] = self.username
        medico['crm'] = self.crm
        medico['duracao_consulta'] = self.duracao_consulta

        return medico

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __unicode__(self):
        return self.first_name


class Especializacao(models.Model):
    nome = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.nome

    def json(self):
        e = {}
        e['id'] = self.id
        e['nome'] = self.nome
        return e 

class Horario(models.Model):
    medico = models.ForeignKey('Medico')

    dia = models.PositiveSmallIntegerField(blank=False)
    hora_inicio = models.TimeField(blank=False)
    hora_final = models.TimeField(blank=False)

    def __unicode__(self):
        return self.dia + ': ' + hora_inicio + ' - ' + hora_final


class Convenio(models.Model):
    """docstring for Convenio"""
    cnpj = models.CharField(max_length=16, primary_key=True)
    razao_social = models.CharField(max_length=80)

    def __unicode__(self):
        return self.razao_social

    def json(self):
        convenio = {}
        convenio['cnpj'] = self.cnpj
        convenio['razao_social'] = self.razao_social
        return convenio

class Consulta(models.Model):
    """docstring for Convenio"""
    id = UUIDField(primary_key=True, auto=True)

    cliente = models.ForeignKey('Cliente')
    medico = models.ForeignKey('Medico')
    data_hora = models.DateTimeField(blank=False)
    checkin = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id