# -*- coding: utf-8 -*-
import random

#Para escolher sempre um mesmo número
#random.seed(2)

numero = random.randint(0, 10) #Qual número começará a busca até qual número poderá ir.
print(numero)

#Método para selecionar um número de uma lista
lista = [5, 66, 42, 12, 1, 5]
numero2 = random.choice(lista)
print(numero2)