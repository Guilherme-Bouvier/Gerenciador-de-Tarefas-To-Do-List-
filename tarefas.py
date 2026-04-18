import json
import os
lista_tarefas = []



def adicionar_tarefa(descricao):
    descricao = descricao.strip()
    
    for t in lista_tarefas:
        if t["descricao"].lower() == descricao.lower():
            print("Já existe uma tarefa com esse nome!")
            return
    
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    
    lista_tarefas.append(tarefa)
    salvando_arquivo()
    print("Tarefa criada com sucesso!")

def listar_tarefas():
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i in range(len(lista_tarefas)):
        tarefa = lista_tarefas[i]
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"{i} - {status} {tarefa['descricao']}")


def concluir_tarefa(indice):
    try:
        lista_tarefas[indice]["concluida"] = True
        salvando_arquivo()

    except IndexError:
        print("Índice inválido. Tente novamente.")

def remover_tarefa(indice):
    try:
        lista_tarefas.pop(indice)
        salvando_arquivo()
        

    except IndexError:
        print("Índice inválido.")


def salvando_arquivo ():
    try:
        with open("tarefas.json", "w") as arquivo:
            json.dump(lista_tarefas, arquivo,)

    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")
    
def carregar_dados():
    global lista_tarefas
    try:
        with open("tarefas.json", "r") as arquivo:
            lista_tarefas = json.load(arquivo)

    except FileNotFoundError:
        lista_tarefas = []
        print("Arquivo não encontrado. Criando lista vazia.")

    except Exception as e:
        lista_tarefas = []
        print(f"Erro ao ler tarefas: {e}")

def limpar_tela():
    os.system("cls")