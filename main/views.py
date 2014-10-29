# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.http import Http404, HttpResponseBadRequest, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.shortcuts import *
from models import *
import linecache
import sys
import json


TAMANHO_MINIMO_SENHA = 6

def is_admin(user):
    return user.is_admin or user.is_staff

def is_cliente(user):
    return user.is_cliente

def is_medico(user):
    return user.is_medico

def is_medico_or_cliente(user):
    return (user.is_medico or user.is_cliente)

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
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        senha =  request.POST['senha']
        confirmar_senha =  request.POST['confirmar_senha']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        cpf = request.POST['cpf']
        rg = request.POST['rg']

        erro = False

        if nome is None or nome =='':
            messages.error(request, "Nome é obrigatrio!")
            erro = True
        
        if sobrenome is None or sobrenome =='':
            messages.error(request, "Sobrenome é obrigatório!")
        
        if senha is None or senha == '':
            # Define erro
            messages.error(request, 'Senha é obrigatória.')
            erro = True

        elif confirmar_senha is None or confirmar_senha == '':
            # Define erro
            messages.error(request, 'Confirmar Senha é obrigatório.')
            erro = True

        elif senha != confirmar_senha:
            # Define erro
            messages.error(request, 'Senhas diferentes.')
            erro = True

        elif len(senha) < TAMANHO_MINIMO_SENHA:
            # Define erro
            messages.error(request, 'A senha deve ter no mínimo 6 caracteres.')
            erro = True

        if email is None or email =='':
            messages.error(request, "Email é obrigatório!")

        if rg is None or rg =='':
            messages.error(request, "RG é obrigatório!")

        if cpf is None or cpf =='':
            messages.error(request, "CPF é obrigatório!")

        if not erro:
            #Tenta salvar o novo cliente no banco
            try:
                #A operacao deve ser atomica
                with transaction.atomic():
                    #Cria usuario
                    cliente = Cliente.objects.create_user(username=email, first_name=nome, last_name=sobrenome, password=senha)
                  
                    #Insere os campos obrigatorios
                    cliente.rg = rg
                    cliente.cpf = cpf
                    cliente.is_cliente = True

                    #Caso existentes, insere os campos nao obrigatorios
                    if telefone and telefone != '':
                        cliente.telefone = telefone

                    if endereco and endereco != '':
                        cliente.endereco = endereco
   
                    #Da um commit no bd
                    cliente.save()

                messages.info(request, "Cadastro realizado com sucesso!")
            except Exception, e:
                #Para qualquer problema, retorna um erro interno                
                PrintException()
                if 'username' in e.message:
                    messages.error(request, 'Email já cadastrado. Escolha outro email.')
                else:
                    messages.error(request, 'Erro desconhecido ao salvar a especialização.')


        return render_to_response('main/cliente/cadastro.html', context)

    else:

        return HttpResponse('Método Não Permitido',status=405)


@login_required        
def conta(request):
    '''
    Esta função é responsável por gerenciar as informacoes de conta.
    
    Esta função aceita pedidos GET e POST

    GET:
        Retorna a página com informacoes da conta do usuario autenticado.

    POST:
        Salva as alteracoes na conta.

    '''
    # TODO !!!

    return HttpResponse('Não Implementado',status=501)

@login_required        
@user_passes_test(is_admin)
def medicos(request):
    '''
    Esta função é responsável retornar uma lista com todos os medicos registrados.
    
    Esta função aceita apenas pedidos GET 

    '''
    context = RequestContext(request)

    if request.method == 'GET':
        #Obtem todos os medicos do bd
        medicos = [m for m in Medico.objects.all()]

        #Retorna a página de todos os medicos
        return render_to_response('main/medico/todos.html', { 'medicos' : medicos }, context)
    else:

        return HttpResponse('Método Não Permitido',status=405)

@login_required        
@user_passes_test(is_admin)
def registrar_medico(request):
    '''
    Esta função é responsável por registrar um novo médico.
    
    Esta função aceita pedidos GET e POST

    GET:
        Retorna a página de cadastro

    POST:
        Realiza o cadastro de um novo médico

    '''
    context = RequestContext(request)

    if request.method == 'GET':
        #Retorna a página de cadastro de cliente
        return render_to_response('main/medico/cadastro.html', context)

    elif request.method == 'POST':
        #obtem dados do POST
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        senha =  request.POST['senha']
        confirmar_senha =  request.POST['confirmar_senha']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        cpf = request.POST['cpf']
        rg = request.POST['rg']
        crm = request.POST['crm']
        duracao_consulta = request.POST['duracao_consulta']

        erro = False

        if nome is None or nome =='':
            messages.error(request, "Nome é obrigatrio!")
            erro = True
        
        if sobrenome is None or sobrenome =='':
            messages.error(request, "Sobrenome é obrigatório!")
        
        if senha is None or senha == '':
            # Define erro
            messages.error(request, 'Senha é obrigatória.')
            erro = True

        elif confirmar_senha is None or confirmar_senha == '':
            # Define erro
            messages.error(request, 'Confirmar Senha é obrigatório.')
            erro = True

        elif senha != confirmar_senha:
            # Define erro
            messages.error(request, 'Senhas diferentes.')
            erro = True

        elif len(senha) < TAMANHO_MINIMO_SENHA:
            # Define erro
            messages.error(request, 'A senha deve ter no mínimo 6 caracteres.')
            erro = True

        if email is None or email =='':
            messages.error(request, "Email é obrigatório!")

        if rg is None or rg =='':
            messages.error(request, "RG é obrigatório!")

        if cpf is None or cpf =='':
            messages.error(request, "CPF é obrigatório!")

        if crm is None or crm =='':
            messages.error(request, "CRM é obrigatório!")

        if duracao_consulta is None or duracao_consulta =='':
            messages.error(request, "Duração da Consulta é obrigatório!")

        if not erro:
            #Tenta salvar o novo cliente no banco
            try:
                #A operacao deve ser atomica
                with transaction.atomic():
                    #Cria usuario
                    medico = Medico.objects.create_user(username=email, first_name=nome, last_name=sobrenome, password=senha, duracao_consulta=duracao_consulta)
                  
                    #Insere os campos obrigatorios
                    medico.rg = rg
                    medico.cpf = cpf
                    medico.crm = crm
                    medico.is_medico = True

                    #Caso existentes, insere os campos nao obrigatorios
                    if telefone and telefone != '':
                        medico.telefone = telefone

                    if endereco and endereco != '':
                        medico.endereco = endereco
   
                    #Da um commit no bd
                    medico.save()

                messages.info(request, "Cadastro realizado com sucesso!")
            except Exception, e:
                #Para qualquer problema, retorna um erro interno                
                PrintException()
                if 'username' in e.message:
                    messages.error(request, 'Email já cadastrado. Escolha outro email.')
                else:
                    messages.error(request, 'Erro desconhecido ao salvar o medico.')


        return render_to_response('main/medico/cadastro.html', context)

    else:

        return HttpResponse('Método Não Permitido',status=405)

@login_required        
@user_passes_test(is_admin)
def especializacoes(request):
    '''
    Esta função é responsável mostrar todas as especializacoes.
    
    Esta função aceita apenas pedidos GET

    '''

    context = RequestContext(request)

    if request.method == 'GET':
        #Obtem todas as especialozacoes
        especializacoes =  [e.json() for e in Especializacao.objects.all()]
        #Retorna a página de tdas as espocializacoes
        return render_to_response('main/especializacao/todas.html',{'especializacoes' : especializacoes}, context)
    else:
        return HttpResponse('Método Não Permitido',status=405)

@login_required        
@user_passes_test(is_admin)
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

        #Obtem o parametro do POST
        espec_nome = request.POST['especializacao']

        erro = False

        if espec_nome is None or espec_nome == '':
            # Define erro
            messages.error(request, 'Nome da especialização inválido.')
            erro = True

        if not erro:
            #Tenta salvar a especializacao no banco
            try:
                #A operacao deve ser atomica
                with transaction.atomic():
                    espec = Especializacao(nome=espec_nome)
                    espec.save()

                messages.info(request, "Cadastro da especialização '{}' realizado com sucesso!".format(espec_nome))
            except Exception, e:
                #Para qualquer problema, retorna um erro interno                
                PrintException()
                if 'unique' in e.message:
                    messages.error(request, 'Especialização já existente.')
                else:
                    messages.error(request, 'Erro desconhecido ao salvar a especialização.')

        return render_to_response('main/especializacao/cadastro.html', context)
    else:
        return HttpResponse('Método Não Permitido',status=405)


@login_required        
@user_passes_test(is_admin)
def convenios(request):
    '''
    Esta função é responsável mostrar todos os convenios.
    
    Esta função aceita apenas pedidos GET

    '''

    context = RequestContext(request)

    if request.method == 'GET':
        #Obtem todas as especialozacoes
        convenios =  [c.json() for c in Convenio.objects.all()]
        #Retorna a página de tdas as espocializacoes
        return render_to_response('main/convenio/todos.html',{'convenios' : convenios}, context)
    else:
        return HttpResponse('Método Não Permitido',status=405)

@login_required        
@user_passes_test(is_admin)
def registrar_convenio(request):
    '''
    Esta função é responsável por registrar uma nova especialização.
    
    Esta função aceita pedidos GET e POST

    GET:
        Retorna a página de cadastro

    POST:
        Realiza o cadastro de um novo convenio

    '''

    context = RequestContext(request)

    if request.method == 'GET':
        #Retorna a página de cadastro de cliente
        return render_to_response('main/convenio/cadastro.html', context)

    elif request.method == 'POST':

        #Obtem o parametro do POST
        cnpj = request.POST['cnpj']
        razao_social = request.POST['razao_social']

        erro = False

        if razao_social is None or razao_social == '':
            # Define erro
            messages.error(request, 'Razão social é obrigatório.')
            erro = True

        if cnpj is None or cnpj == '':
            # Define erro
            messages.error(request, 'CNPJ é obrigatório.')
            erro = True

        if not erro:
            #Tenta salvar a especializacao no banco
            try:
                #A operacao deve ser atomica
                with transaction.atomic():
                    convenio = Convenio(cnpj=cnpj, razao_social=razao_social)
                    convenio.save()

                messages.info(request, "Cadastro do convênio '{}' realizado com sucesso!".format(razao_social))
            except Exception, e:
                #Para qualquer problema, retorna um erro interno                
                PrintException()
                if 'unique' in e.message:
                    messages.error(request, 'Convênio já existente.')
                else:
                    messages.error(request, 'Erro desconhecido ao salvar o convênio.')

        return render_to_response('main/convenio/cadastro.html', context)
    else:
        return HttpResponse('Método Não Permitido',status=405)

@login_required        
@user_passes_test(is_medico)
def horarios(request):
    '''
    Esta função é responsável mostrar todos os horarios do medico autenticado.
    
    Esta função aceita apenas pedidos GET

    '''
    # TODO !!!
    return HttpResponse('Não Implementado',status=501)

@login_required        
@user_passes_test(is_medico)
def registrar_horario(request):
    '''
    Esta função é responsável por registrar um novo horario.
    
    Esta função aceita pedidos GET e POST

    GET:
        Retorna a página de cadastro

    POST:
        Realiza o cadastro de um novo horario.

    '''
    # TODO !!!

    return HttpResponse('Não Implementado',status=501)


@login_required        
@user_passes_test(is_medico_or_cliente)
def consultas(request):
    '''
    Esta função é responsável mostrar todos as consultas do medico ou cliente autenticado.
    
    Esta função aceita apenas pedidos GET

    '''
    # TODO !!!

    return HttpResponse('Não Implementado',status=501)

@login_required        
@user_passes_test(is_cliente)
def registrar_consulta(request):
    '''
    Esta função é responsável por registrar uma nova consulta.
    
    Esta função aceita pedidos GET e POST

    GET:
        Retorna a página de cadastro

    POST:
        Realiza o cadastro de uma nova consulta.

    '''
    # TODO !!!
    context = RequestContext(request)
    if request.method == 'GET':
        return render_to_response('main/consultas/nova.html', context)

@login_required
@user_passes_test(is_admin)
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

