print('Bem vindo a loja de Guilherme Mendes Ferraz')
print(43 * '-')
valor = int(input('Qual é o valor do produto? - '))
quant = int(input('Qual é a quantidade do produto? - '))
total = valor * quant # Valor sem desconto
print(f'O valor sem desconto foi de {total:.2f}')

# ---------- Cálculo do Desconto ----------

desconto = 0
if quant <= 9:
  total = total*1     # Valor sem desconto
  desconto = 0
elif quant >= 10 and quant <= 99:
  total = total*0.95  # Valor com 5% de desconto, ou seja 1 - 0.05
  desconto = 5
elif quant >= 100 and quant <= 999:
  total = total*0.90  # Valor com 10% de desconto, ou seja 1 - 0.10
  desconto = 10
else:
  total = total*0.85  # Valor com 15% de desconto, ou seja 1 - 0.15
  desconto = 15

print('O valor com desconto foi de {:.2f} (desconto {}%)'.format(total, desconto))