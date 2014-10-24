from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Medico)
admin.site.register(Especializacao)
admin.site.register(Horario)
admin.site.register(Convenio)
admin.site.register(Consulta)

