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





#

# 1. A Biblioteca: No topo do tarefas.py, importe a biblioteca json.

# 2. Salvando: Crie a função salvar_dados(). Use with open("dados.json", "w") e json.dump() para gravar a lista
# inteira.

# 3. Carregando: Crie a função carregar_dados(). Use o modo leitura ("r") e json.load() com um try/except
# FileNotFoundError.

# 4. A Integração: Chame carregar_dados() no início do main.py, e chame salvar_dados() toda vez que uma tarefa
# for adicionada ou concluída!