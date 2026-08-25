texto = ["Lorem ipsum dolor sit amet, Os operadores gráficos e tipográficos sabem disso bem na realidade."]
contador = 0

for frase in texto:
    palavras = frase.split()
    contador += len(palavras)

print(f'O texto possui {contador} palavras.')

palavra = 'Os'
encontrada = False
cout = 0
for frase in texto:
    for palavra_do_texto in frase.split():
        cout += 1
        if palavra_do_texto == palavra:
            encontrada = True
            break

if encontrada:
    print(f'A palavra "{palavra}" foi encontrada no texto. Na posição {cout} da contagem de palavras.')
else:
    print(f'A palavra "{palavra}" não foi encontrada no texto.')