num = float(input('Quantos R$ você tem? '))
dolar = 3.27
tot = num / dolar
print('Com R${:.2f} você poderá comprar U${:.2f}'.format(num, tot))