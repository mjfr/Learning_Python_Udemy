# -*- coding: utf-8 -*-

#Sets permitem apenas valores únicos, diferente de tuplas e listas

x = set()
print(type(x))

x.add(1)
print(x)

#Ao repetir um valor existente, ele simplesmente será ignorado
x.add(1)
print(x)

lista = [11, 11, 11, 22, 22, 3, 4, 1, 2, 2]
set_lista = set(lista)

print('\n\n')
print(lista)
print('\n')
print(set_lista)

#Boolean, em sua definição é uma estrutura de dados de verdadeiro ou falso
a = True
b = False
print(a, '\n', b)
print(1 <= 3)
print(3 <= 1)