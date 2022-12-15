print('Bem-vindo ao Controle de Estoque da bicicletaria do Guilherme Mendes Ferraz S.A')
pecas = {} # dicionário usado para adicionar as peças
i = 1 # variável global para criar os códigos das peças
def main():
  while True:
    print('1 - Cadastrar peças\n' + '2 - Consultar peças\n' + '3 - Remover peças\n' + '4 - Sair')
    opcao = int(input('>> '))
    if opcao == 1:
      cadastrarPeca()
    elif opcao == 2:
      consultarPeca()
    elif opcao == 3:
      removerPeca()
    else: # Se for 4 sair com o break
      break

def cadastrarPeca():
  while True:
    global i
    print('Código da peça 00' + str(i)) # Concatenando string com number
    # Pegando os dados:
    nome = input('Qual é o NOME da peça? ')
    fabricante = input('Qual é o FABRICANTE da peça? ')
    valor = input('Qual é o VALOR da peça? ')
    peca = [] # Criando uma lista para adicionar no dicionário pecas, e também limpando ele quando for adicionado mais itens
    # Adicionando os dados na lista
    peca.append(nome)
    peca.append(fabricante)
    peca.append(valor)
    # Adicionando a lista no dicionário
    pecas[i] = peca
    # Somando a variável global i para o código ser diferente na próxima vez
    i = i + 1
    print('')
    break

def consultarPeca():
  print('Voce selecionou a Opção de Consultar Peças.\nEscolha a opção desejada: ')
  print('1 - Consultar todas as peças.\n2 - Consultar Peças por Código\n3 - Consultar Peças por Fabricante\n4 - Retornar')
  opcao = int(input('>> '))
  # O índice 0 é para o nome da peça
  # O índice 1 é para o nome do fabricante
  # O índice 2 é para o valor da peça
  # Enquanto que a chave é o código
  if opcao == 1:
    for i in pecas:
      print(15 * '-')
      print(f'Código: {i}\n' + f'Nome: {pecas[i][0]}\n' + f'Fabricante: {pecas[i][1]}\n' + f'Valor: {pecas[i][2]}')
      print(15 * '-')
  elif opcao == 2:
    codigo = int(input('Digite o código da peça: '))
    for i in pecas:
      if i == codigo:
        print(15 * '-')
        print(f'Código: {i}\n' + f'Nome: {pecas[i][0]}\n' + f'Fabricante: {pecas[i][1]}\n' + f'Valor: {pecas[i][2]}')
        print(15 * '-')
  elif opcao == 3:
    nome = input('Digite o FABRICANTE da peça: ')
    for i in pecas:
      if nome == pecas[i][1]:
        print(15 * '-')
        print(f'Código: {i}\n' + f'Nome: {pecas[i][0]}\n' + f'Fabricante: {pecas[i][1]}\n' + f'Valor: {pecas[i][2]}')
        print(15 * '-')
def removerPeca():
  codigo = int(input('Qual é o código da peça a ser removida: '))
  for i in pecas: # Vai 'andar' por todo o dicionário até achar o código
    if i == codigo:
      del pecas[codigo]
      break # Quando achá-lo não há mais necessidade de procurar então saímos do programa
main() #Chama a função principal depois de ler todo o código, só assim chamará as outras funções.