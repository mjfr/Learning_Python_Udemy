# -*- coding: utf-8 -*-

#Modo normal de elevar valores de uma lista ao quadrado

x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

#Modo usando o list comprehension para elevar valores de uma lista ao quadrado
#Sintaxe: VARIÁVEL = [VALOR_A_ADICIONAR LAÇO CONDIÇÂO]
z = [i ** 2 for i in x]
print(z)

z_condicao = [i for i in x if i%2 == 1]
print(z_condicao)