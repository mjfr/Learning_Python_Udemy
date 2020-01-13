# -*- coding: utf-8 -*-

x = 2
y = 3
z = 3
soma = x + y

"""
Operadores RELACIONAIS
== para verificar se são iguais
!= para verificar se são diferentes
>  para verificar se são maiores
<  para verificar se são menores
>= para verificar se são maiores ou iguais
<= para verificar se são menores ou iguais
"""

print(soma)
print(soma == y)
print(soma != y)
print(soma < y)
print(soma > y)
print(soma <= y)
print(soma >= y)

"""
Operadores LÓGICOS
AND para duas condições serem verdadeiras
OR  para pelo menos uma condição ser verdadeira
NOT para inverter o valor da condição
"""

print(x == y and x == soma) #false
print(y == z and x != soma) #true
print(x == y or x == z) #false
print(x == y or y == z) #true
print(not x == y and not x == soma) #true
print(y == z and not x != soma) #false
