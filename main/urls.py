# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.conf.urls import patterns, include, url
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


		#URL para cadastro de novos clientes
        url(r'^clientes/registrar$','main.views.registrar_cliente',name='registrar_cliente'),

     	#URL para leitura de QRCode
		url(r'^qrCodeScanner$','main.views.qrCodeScan',name='qrCodeScan'),

		#URL para leitura de QRcode decodificado no banco
		url(r'^qrCodeScanner/scancode$','main.views.searchCode',name='scancode'),

		#URL para cadastro de novas especializações
		url(r'^especializacao/registrar$','main.views.registrar_especializacao',name='registrar_especializacao'),

        #Retorna as informações de um salão especifico
        #url(r'^api/saloes/(?P<nome_salao>[a-zA-Z0-9\-]+)$','main.views.api_salao',name='api_salao'),

)
