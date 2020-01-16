# -*- coding: utf-8 -*-

#Escreva um programa que ordene uma lista numérica com três elementos
print("Ordenador de lista numérica")

lista = []
i = 0

while i < 3:
    numero = input("[" + str(i) + "]Digite um número: ")
    lista.append(int(numero))
    i += 1

lista_ordenada = sorted(lista)
print("Lista desordenada: " + str(lista))
print("Lista ordenada" + str(lista_ordenada))

#Att: A resposta poderia ter sido feita em algorítmos de ordenação, como selection sort, merge sort, etc...