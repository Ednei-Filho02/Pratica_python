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

def filter_concluida(tarefas):
    if tarefas == []:
            return print('Sem tarefas . . . ')
    tarefas_concluidas = [tarefa for tarefa in tarefas if tarefa['concluida'] is True]
    if not tarefas_concluidas:
        print("Nenhuma tarefa concluída.")
        return

    for i, tarefa in enumerate(tarefas_concluidas):
        print(f"{i + 1}. {tarefa['descricao']} - Concluída")

def filter_pendente(tarefas):
    if tarefas == []:
        return print('Sem tarefas . . . ')
    tarefas_pendentes = [tarefa for tarefa in tarefas if tarefa['concluida'] is False]
    if not tarefas_pendentes:
        print("Todas as tarefa estão concluídas.")
        return

    for i, tarefa in enumerate(tarefas_pendentes):
        print(f"{i + 1}. {tarefa['descricao']} - Pendente")

def main():
    print("Bem-vindo ao Gerenciador de Tarefas!")