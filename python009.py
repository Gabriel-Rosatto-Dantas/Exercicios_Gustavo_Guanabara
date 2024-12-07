numero = int(input('Digite um número:'))

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero_lista in lista_numeros:
    resultado = numero * numero_lista
    print(numero, 'x', lista_numeros[0], '=', resultado)