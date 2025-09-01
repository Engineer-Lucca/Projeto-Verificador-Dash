
#Código feito pelo Engineer-Lucca <-|->
#O código detalhado está logo abaixo , aproveitem, qualquer dúvida só me chamar via chat  : 

def verificar_hashes(lista_de_pares):
  """
  Recebe uma lista de pares de hashes e compara cada par.
  Para cada par, imprime 'Correto' se forem iguais e 'Inválido' se forem diferentes.

  Args:
    lista_de_pares: Uma lista de listas, onde cada lista interna contém
                    dois hashes. Ex: [['hash1', 'hash1'], ['hash2', 'hash3']]
  """
  # Percorre cada par de hash na lista fornecida
  for par in lista_de_pares:
    # O primeiro item do par é o hash calculado (índice 0)
    hash_calculado = par[0]
    # O segundo item é o hash esperado (índice 1)
    hash_esperado = par[1]

    # Compara os dois hashes
    if hash_calculado == hash_esperado:
      print("Correto")
    else:
      print("Inválido")

# --- Parte Principal do Programa ---

# 1. Lê a entrada diretamente, sem mostrar uma mensagem.
#    Isto é essencial para sistemas de teste automático.
entrada_do_utilizador = input()

# 2. Prepara a lista para a função
hashes_para_verificar = []

# 3. Processa a entrada do utilizador
# Primeiro, divide a string inteira em pares usando o ';' como separador
pares_brutos = entrada_do_utilizador.split(';')

# Para cada par bruto na lista de pares
for par in pares_brutos:
  # Verifica se o par não está vazio antes de processar
  if par:
    # Divide o par em hash calculado e hash esperado usando a ',' como separador
    hashes = par.split(',')
    
    # Garante que o par foi bem formado (tem exatamente duas partes)
    if len(hashes) == 2:
      # **CORREÇÃO IMPORTANTE**: Usa .strip() para remover espaços em branco
      # antes e depois de cada hash antes de adicioná-los à lista.
      hash1_limpo = hashes[0].strip()
      hash2_limpo = hashes[1].strip()
      hashes_para_verificar.append([hash1_limpo, hash2_limpo])

# 4. Chama a função para verificar os hashes, se houver algum
if hashes_para_verificar:
  verificar_hashes(hashes_para_verificar)