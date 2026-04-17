import json

lista_tarefas = []



def adicionar_tarefa(descricao):
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    lista_tarefas.append(tarefa)


def listar_tarefas():
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
      

    for tarefa in lista_tarefas:
        print(f"- {tarefa['descricao']}")
        
        for i, tarefa in enumerate(lista_tarefas):
            status = "[X]" if tarefa["concluida"] else "[ ]"
            print(f"{i} - {status} {tarefa['descricao']}")
        

def concluir_tarefa(indice):
    try:
        lista_tarefas[indice]["concluida"] = True
        print("Tarefa concluída com sucesso!")
    except IndexError:
        print("Índice inválido. Tente novamente.")
