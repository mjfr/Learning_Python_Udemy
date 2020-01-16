# -*- coding: utf-8 -*-

#Modo normal de imprimir uma lista com seus índices
lista = ["Abacaxi", "Bola", "Cachorro", "Ferro"]

for i in range(len(lista)):
    print(i, lista[i])

#Modo utilizando enumerate
for i, nome in enumerate(lista):
    print(i, nome)