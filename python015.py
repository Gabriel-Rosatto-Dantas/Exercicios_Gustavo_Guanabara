km = float(input('Informe a quantidade de kilometragem:'))
dias = float(input('Informe quanto dias:'))
calculo_km = km * 0.15
calculo_carro = dias * 60

preco_total = calculo_km + calculo_carro

print(f'Neste caso, custará R${preco_total}')
