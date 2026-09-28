# utilizando o conceito feito em cadastro-media.py, 
# vamos criar um programa que consiga inseruir vários alunos e suas notas, calcular a média de cada um e exibir o resultado final.

# Lista para armazenar os dados de cada aluno
alunos = []

# Loop para cadastrar vários alunos
while True:

    # Pegando o nome do aluno
    nome = input('Digite o nome do aluno: ')

    # Lista de notas do aluno atual
    notas = []

    # Loop para pegar as 3 notas
    for i in range(3):

        # Loop para repetir enquanto a nota for inválida
        while True:
            try:
                nota = float(
                    input(f'Insira a nota {i + 1}: ').replace(',', '.')
                )

                # Verifica se a nota está entre 0 e 10
                if nota < 0 or nota > 10:
                    raise ValueError

                notas.append(nota)
                break

            except ValueError:
                print('Erro: digite uma nota válida entre 0 e 10.')

    # Guardando nome e notas juntos
    alunos.append({
        'nome': nome,
        'notas': notas
    })

    # Verifica se deseja cadastrar outro aluno
    controle = input('Deseja adicionar outro aluno? (s/n): ')

    if controle.lower() != 's':
        break


# Exibindo os resultados
print('\n===== RESULTADO =====')

for aluno in alunos:

    nome = aluno['nome']
    notas = aluno['notas']

    # Calculando a média
    media = sum(notas) / len(notas)

    # Determinando a situação
    estado = (
        'Aprovado' if media >= 7
        else 'Recuperação' if media >= 5
        else 'Reprovado'
    )

    # Exibindo o resultado
    print(f'\nAluno: {nome}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {estado}')