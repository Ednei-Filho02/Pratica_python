'''
Pacote pip é um sistema de gerenciamento de pacotes usado para instalar e gerenciar bibliotecas e dependências em projetos Python.
Ele permite que os desenvolvedores compartilhem e reutilizem código facilmente, facilitando a instalação de pacotes de terceiros.
O pip é amplamente utilizado na comunidade Python e é a ferramenta padrão para instalar pacotes do Python Package Index (PyPI), 
que é o repositório oficial de pacotes Python. Com o pip, os desenvolvedores podem instalar, atualizar e remover pacotes de forma 
simples e eficiente, tornando o processo de gerenciamento de dependências mais fácil e organizado.
Para instalar um pacote usando o pip, você pode usar o seguinte comando no terminal ou prompt de comando:
pip install nome_do_pacote
e para desinstalar um pacote, você pode usar:
pip uninstall nome_do_pacote
'''

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))