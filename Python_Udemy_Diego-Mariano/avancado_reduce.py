# -*- coding: utf-8 -*-

from functools import reduce

lista = [1, 3, 5, 10, 20, 33]

#Método normal de fazer obter a soma de uma lista
def soma(x, y):
    return x+y

soma_i = 0
for i in lista:
    soma_i += i
print(soma_i)

print("\n/////////////////\n")

#Recebe uma lista e retorna um único valor da lista. Ex.: Obter a soma de todos os valores de uma lista
#É necessário importar
soma = reduce(soma, lista)
print(soma)