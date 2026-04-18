from tarefas import carregar_dados, adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa, limpar_tela

import time

tempo = 2

carregar_dados()

while True:
    limpar_tela()

    print("\n=== GERENCIADOR DE TAREFAS ===\n")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        limpar_tela()
        print("===========LISTA DE TAREFAS==========\n")
        descricao = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(descricao)
        time.sleep(tempo)

    elif opcao == "2":
        limpar_tela()
        print("===========LISTA DE TAREFAS==========\n")
        listar_tarefas()
        time.sleep(tempo)

    elif opcao == "3":
        limpar_tela()
        print("===========TAREFAS CONCLUÍDAS==========\n")
        listar_tarefas()
        
        try:
            indice = int(input("\nDigite o número da tarefa: "))
            concluir_tarefa(indice)
            print("Tarefa concluída com sucesso!\n")
            listar_tarefas()

        except ValueError:
            print("Digite um número válido.")
        time.sleep(tempo)

    elif opcao == "4":
        limpar_tela()
        print("===========REMOVER TAREFAS==========\n")
        listar_tarefas()

        try:
            indice = int(input("\nDigite o número da tarefa para remover: "))
            remover_tarefa(indice)
            print("Tarefa removida com sucesso!\n")
                        
        except ValueError:
            print("Digite um número válido.")

        time.sleep(tempo)

    elif opcao == "5":
        limpar_tela()
        print("Encerrando o programa...")
        break
        
    else:
        print("Opção inválida.")
        limpar_tela()
        time.sleep(tempo)