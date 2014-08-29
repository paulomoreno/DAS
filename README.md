DAS
===

O DAS (Doctor Appointment System) é um projeto para a disciplina de Tópicos Avançados em Comunicação, ministrada pelo Professor Doutor Edson dos Santos Moreira.

O Sistema
=========

O Sistema DAS é dividido em duas partes. O Backend é a parte que fica no servidor e faz todo o processamento e gerencia os dados. O Frontend, consiste na interface do usuário com o Backend (o site).

Backend
-------

O desenolvimento do Backend é realizado através da framework Django 1.6 com as dependencias citadas abaixo, em Python 2.7.3.

O Projeto em Django possui apenas um aplicativo, chamado de *main* ([source/main/](https://github.com/paulomoreno/DAS/tree/master/source/main)). Dentor dele, existem 4 arquivos principais:

#### models.py
([source/main/models.py](https://github.com/paulomoreno/DAS/tree/master/source/main/models.py))

Um ORM para definição do modelo relacional a ser utilizado pelo SGBD para a construção do BD. Todos os modelos estão descritos neste arquivo e são necessários tanto para a criação dos mesmo pelo SGBD quanto para o uso por parte da framework do Django.

#### urls.py
([source/main/urls.py](https://github.com/paulomoreno/DAS/tree/master/source/main/urls.py))

Este arquivo contêm todas as URL's do aplicativo main, e linka cada uma delas a uma view. Todas as urls do site são definidas neste arquivo.

#### views.py
([source/main/views.py](https://github.com/paulomoreno/DAS/tree/master/source/main/views.py))

Neste arquivo estão definidas todas as views. Cada view é responsável por interpretar um pedido, autenticar o usuário e retornar o conteúdo requerido caso o usuário tenha permissões ou retornar os devidos erros caso o usuário não tenha permissão ou não esteja autenticado.


Frontend
--------

O site será sendo desenvolvido em HTML, CSS e javascript (com auxilio de JQuery).

Os templates em html podem ser encontrados em ([source/templates/](https://github.com/paulomoreno/DAS/tree/master/source/templates))

Os arquivos estáticos de CSS e Javascript podem ser encontrados em ([source/static/css/](https://github.com/paulomoreno/DAS/tree/master/source/static/css)) e ([source/static/js/](https://github.com/paulomoreno/DAS/tree/master/source/static/js)) respectivamente.

Instalação e Uso
================

Para instalar a utilizar o sistema, são necessários os seguintes passos:

```shell
#Instalar pip install. 
#Aqui utilizo o comando apt-get considerando que estamos num ambiente Ubuntu
#Também considero que apt-get e python 2.7 já estão presentes no sistema
sudo apt-get install python-pip python-dev build-essential
sudo pip install --updgrade pip

#Instalar virtualenv
sudo pip install virtualenv

#Criar um virtualenv
virtualenv das-venv

#Acessar o virtualenv
source das-venv/bin/activate

#Instalar django 1.6 (pelo virtualenv)
pip install Django==1.6.4

#Sair do virtualenv
deactivate
```

Dependências
------------

Após a instalação do ambiente, deverão ser instaladas as dependências:

* [Django Extensions](https://github.com/django-extensions/django-extensions): necessário para o uso do UUID Field.
```shell
#Instalar Django extensions
pip install django-extensions
```

Gerenciando o Banco de Dados
---------------------------

Estamos utilizando o SQLite, mas ele será trocado por um SGBD mais poderoso para a produção. 

*Para iniciar o banco de dados do zero, basta entrar na pasta source/ e executar o seguinte comando:
```shell
python manage.py syncdb
```

Executando o Sistema
--------------------

Para execução do sistema em modo de testes, basta entrar na pasta source/ e executar o seguinte comando:

```shell
python manage.py runserver
```

Este método de rodar o servidor NÃO deverá ser utilizado durante fase de produção, conforme a própria equipe do Django diz.




