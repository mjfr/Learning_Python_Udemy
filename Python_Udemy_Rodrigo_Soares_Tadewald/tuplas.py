# -*- coding: utf-8 -*-

#Um formato de dado utilizado apenas para ter uma integridade maior. Não é tão usada como outras estruturas
#Tuplas são semelhantes a listas. São imutáveis e sua sintaxe tem a diferença na utilização de parênteses
t = (1, ['a', 'b', 3, '4'], 3, 'trio', 3, 3, 3)
print(type(t))
print(t)

#Podemos trabalhar com indexação e contagem de elementos
print(t.index('trio'))
print(t.count(3))