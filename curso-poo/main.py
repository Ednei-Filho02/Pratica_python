# --- Importando a classe Cachorro para ser utilizada
from cachorro import Cachorro

# --- Criação de um objeto (instância) da classe Cachorro
meu_cachorro = Cachorro(apelido="Rex", idade=5, raca="Labrador Retriever") # SAÍDA: Criando um novo cachorro chamado Rex...

# --- Acessando os atributos do objeto
print("\n--- Atributos do Cachorro ---") # SAÍDA: --- Atributos do Cachorro ---
print(f"Apelido: {meu_cachorro.apelido}") # SAÍDA: Apelido: Rex
print(f"Idade: {meu_cachorro.idade} anos") # SAÍDA: Idade: 5 anos
print(f"Raça: {meu_cachorro.raca}") # SAÍDA: Raça: Labrador Retriever

# --- Chamando os métodos do objeto
print("\n--- Ações (Métodos) do Cachorro ---") # SAÍDA: --- Ações (Métodos) do Cachorro ---
meu_cachorro.sentar() # SAÍDA: Rex sentou!
meu_cachorro.rolar() # SAÍDA: Rex rolou no chão!
meu_cachorro.correr() # SAÍDA: Rex está correndo rapidamente.
meu_cachorro.correr(velocidade="lentamente") # SAÍDA: Rex está correndo lentamente.
meu_cachorro.comer("ração") # SAÍDA: Rex está comendo ração

print("\n-----------------------------------") # SAÍDA: -----------------------------------

# --- Criando outro objeto da mesma classe para demonstrar a reutilização
outro_cachorro = Cachorro(apelido="Luna", idade=2, raca="Golden Retriever")
print(f"\nConheça a {outro_cachorro.apelido}, uma {outro_cachorro.raca} de {outro_cachorro.idade} anos.")
outro_cachorro.sentar() # SAÍDA: Luna sentou!