# -*- coding: utf-8 -*-

def pares(i):
    if i % 2 == 0:
        return i

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Recebe uma função que aplicará e uma lista que será analisada
lista_pares = filter(pares, lista)
print(list(lista_pares))
