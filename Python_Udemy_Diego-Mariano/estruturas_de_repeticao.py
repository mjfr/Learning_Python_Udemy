#-*- coding: utf-8 -*-
x = 1

#Laço while
while x < 10:
    print(x)
    x += 1

print("\n\n\n")

#Laço for para percorrer listas
lista = [1,2,3,4,5]
for i in lista:
    print(i)

print("\n\n\n")

#Laço for combinado com a função range (para retornar lista), lembrando que a contagem começa no valor 0
#Mostrará uma lista com quatro números de 0 a 3
for a in range(4):
    print(a)

print("\n\n\n")

#Mostrará uma lista com 4 números de 5 a 8
for b in range(5, 9):
    print(b)

print("\n\n\n")

#Mostrará uma lista com números entre 10 e 20, de 2 em 2
for c in range(10, 20, 2):
    print(c)

print("\n\n\n")