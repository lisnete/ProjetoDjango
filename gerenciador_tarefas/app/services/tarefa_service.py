from ..models import Tarefa

def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo, descricao=tarefa.descricao, data_expiracao=tarefa.data_expiracao, prioridade=tarefa.prioridade)