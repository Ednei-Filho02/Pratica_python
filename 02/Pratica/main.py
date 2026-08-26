import funcoes as f

f.main()
tarefas = []   

while True:
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{i + 1}. {tarefa['descricao']} - {status}")

    print("\nOpções:")
    print("1. Adicionar tarefa")
    print("2. Concluir tarefa")
    print("3. Remover tarefa")
    print("4. Filtrar tarefas concluidas")
    print("5. Filtrar tarefas pendentes")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        f.adicionar_tarefa(tarefas)

    elif opcao == '2':
        f.concluir_tarefa(tarefas)

    elif opcao == '3':
        f.remover_tarefa(tarefas)

    elif opcao == '4':
        f.filter_concluida(tarefas)

    elif opcao == '5':
        f.filter_pendente(tarefas)

    elif opcao == '6':
        print("Saindo da aplicação...")
        break

    else:
        print("Opção inválida. Tente novamente.")