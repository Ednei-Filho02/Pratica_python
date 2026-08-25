def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({'descricao': descricao, 'concluida': False})
    print("Tarefa adicionada com sucesso!")

def concluir_tarefa(tarefas):
    numero = int(input("Digite o número da tarefa a ser concluída: ")) - 1
    if 0 <= numero < len(tarefas):
        tarefas[numero]['concluida'] = True
        print("Tarefa concluída com sucesso!")
    else:
        print("Número de tarefa inválido.")

def remover_tarefa(tarefas):
    numero = int(input("Digite o número da tarefa a ser removida: ")) - 1
    if 0 <= numero < len(tarefas):
        tarefas.pop(numero)
        print("Tarefa removida com sucesso!")
    else:
        print("Número de tarefa inválido.")

def main():
    print("Bem-vindo ao Gerenciador de Tarefas!")

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
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_tarefa(tarefas)

    elif opcao == '2':
        concluir_tarefa(tarefas)

    elif opcao == '3':
        remover_tarefa(tarefas)

    elif opcao == '4':
        print("Saindo da aplicação...")
        break

    else:
        print("Opção inválida. Tente novamente.")