
# Crie um programa que:

# Peça o nome do aluno.
# Peça 3 notas.
# Calcule a média.
# Mostre:
# Aprovado → média >= 7
# Recuperação → média >= 5 e < 7
# Reprovado → média < 5
# Utilize try/except para impedir que o programa quebre caso o usuário 
# digite algo que não seja número nas notas.


# Linha para fazer o input do nome do aluno
aluno = input('Digite o nome do aluno: ')

# inicio da lista de notas
notas = []

# inicio do loop para pegar as 3 notas 
for i in range(3):
    # Loop para pegar as notas 
    while True:
        # Try/except para tratar erro em caso de valor não for valido para nota 
        try:
            # linha de comando para pegar a nota do aluno e usando o .replace para substituir a , por . caso o usuariuo digite e assim não mate o programa 
            nota = float(input(f'Insira a nota {i + 1}: ').replace(',', '.'))
            # Verificação da nota para garantir que pertence ao intervalo de 0 a 10.
            if nota < 0 or nota > 10:
                raise ValueError
            # inserindo a nota a lista de notas[]
            notas.append(nota)
            break

        except ValueError:
            print('Erro: digite uma nota válida entre 0 e 10.')
# calculando a media conforme a soma das notas e da quantidade de notas na lista
media = sum(notas) / len(notas)
# descobrindo se o aluno está aprovado, em recuperação ou reprovado.
estado = (
    'Aprovado' if media >= 7
    else 'Recuperação' if media >= 5
    else 'Reprovado'
)
# exibição do resultado final para o aluno.
print(f'O aluno {aluno} obteve média {media:.2f} e está {estado}.')