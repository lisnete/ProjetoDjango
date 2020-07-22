from django.contrib import admin
from django.urls import path

##importa tudo que esta criado no arquivo views.py
from .views import *


urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
]
