## Os dois códigos tem a mesma função
list1 = []
for valor in range(5):
  list1.append(valor+10)
print(list1)

list2 = [valor+10 for valor in range(5)]
print (list2)
############################

## O código pega os valores de 1 até 30 e mostra os que são divisiveis por 4, os dois tem a mesma função.

list3 = []
for numero in range (1,30):
  if numero % 4 == 0:
    list3.append(numero)
print(list3)

multiplos4 = [numero for numero in range(1,30) if numero % 4 == 0]
print(multiplos4)
#############################

## O código imprime "vermelho" se as notas forem menores do que 6 e "azul" se forem maiores ou iguais a 6.

conceito = ['azul' if nota >= 6 else 'vermelha' for nota in range(1,11)]
print(conceito)