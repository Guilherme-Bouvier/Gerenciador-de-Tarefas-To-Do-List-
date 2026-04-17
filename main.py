from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa


while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(descricao)
        

    elif opcao == "2":
        listar_tarefas()
        

    elif opcao == "3":
        listar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa: "))
            concluir_tarefa(indice)
        except ValueError:
            print("Digite um número válido.")
        


    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")
    