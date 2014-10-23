# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.conf.urls import patterns, include, url
from main import views

urlpatterns = patterns('',

		#Pagina inicial
        url(r'^$','main.views.index',name='index'),

		#URL para cadastro de novos clientes
        url(r'^clientes/registrar$','main.views.registrar_cliente',name='registrar_cliente'),

     	#URL para leitura de QRCode
	    url(r'^qrCodeScan','main.views.qrCodeScan'),

	    #URL para leitura de QRcode decodificado no banco
	    url(r'^qrCodeScan/scancode','main.views.searchCode'),

        #Retorna as informações de um salão especifico
        #url(r'^api/saloes/(?P<nome_salao>[a-zA-Z0-9\-]+)$','main.views.api_salao',name='api_salao'),

)
