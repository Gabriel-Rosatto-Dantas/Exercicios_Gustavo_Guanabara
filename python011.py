largura = float(input('Informe a largura da parede:'))
altura = float(input('Informe a altura da parede:'))
area = altura * largura
qtde_tinta = area * 0.5

print(f'A area total em m2 é {area}, com isso, você precisará de {qtde_tinta}L de tinta para pintar toda a parede.')