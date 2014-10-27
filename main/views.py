# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.http import Http404, HttpResponseBadRequest, HttpResponse
from django.shortcuts import *
from models import *
import json

def api_monta_json(obj_json):
    '''
    Função que retorna um objeto JSON
    '''
    return HttpResponse(json.dumps(obj_json, indent=4), content_type="application/json")

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)


# Create your views here.

def index(request):
    '''
    Função responsável por retornar a página inicial.
    '''
    context = RequestContext(request)

    if request.method == 'GET':
        return render_to_response('main/index.html', context)
    else:
        return HttpResponse('Método Não Permitido',status=405)

def registrar_cliente(request):
    '''
    Esta função é responsável por registrar um novo cliente.
    
    Esta função aceita pedidos GET e POST

    GET:
        Retorna a página de cadastro

    POST:
        Realiza o cadastro de um novo cliente

    '''
    context = RequestContext(request)

    if request.method == 'GET':
        #Retorna a página de cadastro de cliente
        return render_to_response('main/cliente/cadastro.html', context)

    elif request.method == 'POST':
        #obtem dados do POST
        name        = request.POST['nome']
        last_name   = request.POST['sobrenome']
        email       = request.POST['email']
        pwd         =  request['senha']
        checkbox    = request['novidades']
        if name is None or nome =='':
        	messages.error(request, "Campo nome obrigatorio")

        return render_to_response('main/cliente/cadastro.html', context)

    else:

        return HttpResponse('Método Não Permitido',status=405)
        
def registrar_especializacao(request):
    '''
    Esta função é responsável por registrar uma nova especialização.
    
    Esta função aceita pedidos GET e POST

    GET:
        Retorna a página de cadastro

    POST:
        Realiza o cadastro de uma nova especialização

    '''

    context = RequestContext(request)

    if request.method == 'GET':
        #Retorna a página de cadastro de cliente
        return render_to_response('main/especializacao/cadastro.html', context)
    elif request.method == 'POST':
        espec = Especializacao(nome=request.POST['especializacao'] )
        espec.save()

        return render_to_response('main/especializacao/cadastro.html', context)
    else:
        return HttpResponse('Método Não Permitido',status=405)


def qrCodeScan(request):
    '''
    qrCode scanner
    '''
    context = RequestContext(request)
    return render_to_response('main/qrCodeScanner/index.html', context)

def searchCode(request):

    if request.method == 'POST':
        entrada = request.POST['qrCode']

    #Testar entrada
    print(entrada)
    u = Usuario.objects.get(nome=entrada)

    #Buscar no banco

    return api_monta_json({'response':u.get_full_name()})

