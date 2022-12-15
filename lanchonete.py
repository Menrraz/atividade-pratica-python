print('Bem vindo a lanchonete de Guilherme Mendes Ferraz')
print(21 * '-' + 'Cardápio' + '-' * 20)
print('| Código |      Descrição        | Valor |\n' +
      '|  100   |    Cachorro Quente    |  9,00 |\n' +
      '|  101   | Cachorro Quente Duplo | 11,00 |\n' +
      '|  102   |         X-Egg         | 12,00 |\n' +
      '|  103   |       X-Salada        | 12,00 |\n' +
      '|  104   |        X-Bacon        | 14,00 |\n' +
      '|  105   |        X-Tudo         | 17,00 |\n' +
      '|  200   |   Refrigerante Lata   |  5,00 |\n' +
      '|  201   |      Chá Gelado       |  4,00 |\n')
cardapio = {
            100: ['Cachorro Quente', 9], 
            101: ['Cachorro Quente Duplo', 11],
            102: ['X-Egg', 12],
            103: ['X-Salada', 12],
            104: ['X-Bacon', 14],
            105: ['X-Tudo', 17],
            200: ['Refrigerante Lata', 5],
            201: ['Chá Gelado', 4]
            }
soma = 0
while True:
  cod = int(input('Digite o código desejado: '))
 
  try:
    # índice 0 = nome do produto // índice 1 = preço do produto
    print(f'Você pediu {cardapio[cod][0]} no valor de {cardapio[cod][1]:.2f}')
    soma = soma + cardapio[cod][1]
  except KeyError: # Se for digitado alguma opção inválida  
    print('Opção inválida')
    continue
 
  print('Deseja pedir mais alguma coisa?\n' + '1 - Sim\n' + '0 - Não')
  continuar = int(input('>> '))
  if continuar == 1:
    continue # Volta para o ínicio do While
  elif continuar == 0:
    print('O total a ser pago é: {}{}'.format(soma, '.00'))
    break # Saí do programa depois de mostrar o total a ser pago
  else:
    print('Opção inválida')
    continue