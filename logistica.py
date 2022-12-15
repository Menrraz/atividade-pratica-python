print('Bem-vindo a companhia de Logística Guilherme Mendes Ferraz S.A')
print('-' * 62)
def main():
  dimensao = dimensoesObjeto()
  peso = pesoObjeto()
  rota = rotaObjeto()
  print(f'Total a pagar: R${(dimensao*peso*rota):.2f}  (dimensão: {dimensao} * peso: {peso} * rota: {rota})')
 
def dimensoesObjeto():
  while True:
    #Comprimento do objeto
    while True:
      try:
        comprimento = int(input('Digite o comprimento do objeto (em cm): '))
        break
      except ValueError:
        print("Por favor digite valor numérico")
        continue
 
    #Largura do objeto
    while True:
      try:
        largura = int(input('Digite o largura do objeto (em cm): '))
        break
      except:
        print("Por favor digite valor numérico")
        continue
 
    #Altura do objeto
    while True:
      try:
        altura = int(input('Digite o altura do objeto (em cm): '))
        break
      except:
        print("Por favor digite valor numérico")
        continue
    volume = comprimento * altura * largura
    if volume >= 100000:
      print('Não aceitamos objetos com dimensões muito grandes.\nEntre com as dimensões desejadas novamente')
      continue
    else:
      print('O volume do objeto é (em cm³): {}'.format(volume))
      break
  #            volume < 1.000      10$
  # 1.000  <=  volume < 10.000     20$
  # 10.000 <=  volume < 30.000     30$
  # 30.000 <=  volume < 100.000    50$
  #            volume >= 100.000   Não aceito
  if volume < 1000:
    return 10
  elif 1000 <= volume < 10000:
    return 20
  elif 30000 <= volume < 10000:
    return 30
 
def pesoObjeto():
  while True:
    try:
      peso = float(input('Digite o peso do objeto (em kg): '))
    except:
      print('Digite um valor numérico')
      continue
    #        peso <= 0.1              1
    # 0.1 <= peso < 1                 1.5
    # 1   <= peso < 10                2
    # 10  <= peso < 30                3
    #        peso => 30               Não é aceito
    if peso >= 30:
      print('Não aceitamos objetos tão pesados.\nEntre com o peso novamente.')
      continue
    elif 10 <= peso < 30:
      return 3
    elif 1 <= peso < 10:
      return 2
    elif 0.1 <= peso < 1:
      return 1.5
    else:
      return 1
 
def rotaObjeto():
  print('RS - De Rio de Janeiro até São Paulo\nSR - De Brasília até São Paulo\nBS - De Brasília até Rio de Janeiro')
  while True:
    rota = input('Selecione uma rota (RS, SR ou BS): ')
    if rota.lower() == 'rs':
      return 1
    elif rota.lower() == 'sr':
      return 1.2
    elif rota.lower() == 'bs':
      return 1.5
    else: # Quando o usuário digitar qualquer coisa que não RS, SR ou BS
      print('Você selecionou uma rota que não existe.')
      continue
 
main()