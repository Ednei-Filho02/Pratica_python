alunos = ['Matheus', 'Julia', 'Pedro', 'Ana', 'Lucas']
aprovados = []
reprovados = []
recuperacao = []
for alunos in alunos:    
    nota1 = 8.5
    nota2 = 9.3
    nota3 = float(input(f'Insira o valor da terceira nota de {alunos}: ').replace(',', '.'))

    soma = nota1 + nota2 + nota3

    media = soma / 3
    print(f'A media de {alunos} das notas é de: {media:.2f} ')

    if media >=7:
        print(f'{alunos} foi aprovado, com média final de {media:.2f}')
        aprovados.append(alunos)
    elif media >= 5:
        print(f'{alunos} está de recuperação, com média final de {media:.2f}') 
        recuperacao.append(alunos)
    else:
        print(f'{alunos} foi reprovado, com média final de {media:.2f}')
        reprovados.append(alunos)

print(f'Os alunos aprovados foram: {aprovados}')
print(f'Os alunos em recuperação foram: {recuperacao}')
print(f'Os alunos reprovados foram: {reprovados}')