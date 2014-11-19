# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from main import views

urlpatterns = patterns('',

		#Pagina inicial
        url(r'^$','main.views.index',name='index'),

		# Auth - Login
		url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}),
		# Auth - Logout
		url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': 'index'}),
		# Auth - Register
		#url(r'^register$', 'main.views.register', name='register'),

        # ------------------------------------------------------------ #
        #                   Clientes
        # ------------------------------------------------------------ #
        #URL para secretataria visualizar 
        url(r'^clientes$','main.views.clientes',name='clientes'),
		#URL para cadastro de novos clientes
        url(r'^clientes/novo$','main.views.registrar_cliente',name='registrar_cliente'),
		#URL para alterar clientes
        url(r'^clientes/(?P<id>[a-zA-Z0-9\-]+)/alterar$','main.views.alterar_cliente',name='alterar_cliente'),
        #URL para remover clientes
        url(r'^clientes/(?P<id>[a-zA-Z0-9\-]+)/remover$','main.views.remover_cliente',name='remover_cliente'),

        # ------------------------------------------------------------ #
        #                   Medicos
        # ------------------------------------------------------------ #
        #Todos os medicos
        url(r'^medicos$','main.views.medicos',name='medicos'),        
		#URL para cadastro de novos médicos
        url(r'^medicos/novo$','main.views.registrar_medico',name='registrar_medico'),
        #URL para remover medico
        url(r'^medicos/(?P<id>[a-zA-Z0-9\-]+)/remover$','main.views.remover_medico',name='remover_medico'),
        #URL para alterar medicos
        url(r'^medicos/(?P<id>[a-zA-Z0-9\-]+)/alterar$','main.views.alterar_medico',name='alterar_medico'),

        # ------------------------------------------------------------ #
        #                   Secretarias
        # ------------------------------------------------------------ #
        #Todas as secretarias
        url(r'^secretarias$','main.views.secretarias',name='secretarias'),        
        #URL para cadastro de novas secretarias
        url(r'^secretarias/nova$','main.views.registrar_secretaria',name='registrar_secretaria'),
        #URL para remover secretaria
        url(r'^secretarias/(?P<id>[a-zA-Z0-9\-]+)/remover$','main.views.remover_secretaria',name='remover_secretaria'),
        #URL para alterar secretaria
        url(r'^secretarias/(?P<id>[a-zA-Z0-9\-]+)/alterar$','main.views.alterar_secretaria',name='alterar_secretaria'),

        # ------------------------------------------------------------ #
        #                   Convenios
        # ------------------------------------------------------------ #
        #Todos os convenios
		#URL para cadastro de novos convenios
        url(r'^convenios/novo$','main.views.registrar_convenio',name='registrar_convenio'),
        #URL para remover convenio
        url(r'^convenio/(?P<id>[a-zA-Z0-9\-]+)/remover$','main.views.remover_convenio',name='remover_convenio'),
        #URL para editar convenio
        url(r'^convenio/(?P<id>[a-zA-Z0-9\-]+)/alterar$','main.views.alterar_convenio',name='alterar_convenio'),

        # ------------------------------------------------------------ #
        #                   Horarios
        # ------------------------------------------------------------ #
  		#Todos os horarios de um medico
        url(r'^horarios$','main.views.horarios',name='horarios'),        
		#URL para cadastro de novos horarios
        url(r'^horarios/novo$','main.views.registrar_horario',name='registrar_horario'),   
        #URL para cadastro de novos horarios
        url(r'^horarios/(?P<id>[a-zA-Z0-9\-]+)/remover$','main.views.remover_horario',name='remover_horario'),
        #URL para cadastro de novos horarios
        url(r'^horarios/(?P<id>[a-zA-Z0-9\-]+)/alterar$','main.views.alterar_horario',name='alterar_horario'),

        # ------------------------------------------------------------ #
        #                   Consultas
        # ------------------------------------------------------------ #
  		#Todas as consultas de um medico, ou de um cliente (de acordo com o tipo de usuario logado)
        url(r'^consultas$','main.views.consultas',name='consultas'),        
        #URL para cadastro de novas consultas
        url(r'^consultas/cadastro$','main.views.registrar_consulta',name='registrar_consulta'),
        #URL para agendar horario de uma consulta
        url(r'^consultas/registrar_consulta_resumo$','main.views.registrar_consulta_resumo',name='registrar_consulta_resumo'),
        #URL para listar médicos de uma dada especialização
        url(r'^consultas/listarMedicosEspec$','main.views.listar_medico_espec',name='listar_medico_espec'),
        #URL para lista horários disponíveis de um médio
        url(r'^consultas/listarHorario$','main.views.listar_horario',name='listar_horario'),
        #URL para mostrar um QR Code de uma dada consulta
        url(r'^consultas/(?P<id>[^/]+)/ver$','main.views.mostrar_qr_code',name='mostrar_qr_code'),


        # ------------------------------------------------------------- #
        #                   QrCode Scanner
        # ------------------------------------------------------------- #
     	#URL para leitura de QRCode
		url(r'^qrCodeScanner$','main.views.qrCodeScan',name='qrCodeScan'),

		#URL para leitura de QRcode decodificado no banco
		url(r'^qrCodeScanner/scancode$','main.views.searchCode',name='scancode'),

        # ------------------------------------------------------------ #
        #                   Especializacoes
        # ------------------------------------------------------------ #
		#URL para todas as especializações
		url(r'^especializacoes$','main.views.especializacoes',name='especializacoes'),
		#URL para cadastro de novas especializações
		url(r'^especializacoes/nova$','main.views.registrar_especializacao',name='registrar_especializacao'),
		#URL para remover determinada especilizacao
		url(r'^especializacoes/(?P<id>[a-zA-Z0-9\-]+)/remover$','main.views.remover_especializacao',name='remover_especializacao'),
		#URL para alterar determinada especilizacao
		url(r'^especializacoes/(?P<id>[a-zA-Z0-9\-]+)/alterar$','main.views.alterar_especializacao',name='alterar_especializacao'),

        url(r'^fila$','main.views.fila',name='fila'),


        #Retorna as informações de um salão especifico
        #url(r'^api/saloes/(?P<nome_salao>[a-zA-Z0-9\-]+)$','main.views.api_salao',name='api_salao'),

        url(r'^convenios$','main.views.convenios',name='convenios'),       

        #Caso o usuario digite qualquer coisa não prevista acima, retornar erro
        #para evitar que ele veja este arquivo na mensagem de erro
        url(r'.','main.views.avoid_eavesdropping',name='eavesdropping'), 


)
