# -*- coding: utf-8 -*-

#Em Python listas pode ser considerado um dos tipos de dado mais importantes de se dominar.
#A lista não tem tamanho fixo e podem-se ser usados diversos tipos de dados. (Não é computacionalmente muito eficiente.)

my_list = [1, 2, 3]
print(my_list)

my_list2 = [1, 'string', 2.3, []]
print(my_list2)

#Podemos puxar valores por índices de diversas formas
print(my_list2[-1]) #Último índice (contando de trás para frente)
print(my_list2[3]) #Terceiro índice
print(my_list2[:2]) #Até o segundo índice
print(my_list2[2:]) #A partir do segundo índice

#Juntando listas (Assim como strings, é possível "somar")
my_list3 = my_list + my_list2
print(my_list3)

#Também é possível multiplicar listas assim como em strings
print(my_list*5)

#Para saber o tamanho de listas, usamos len()
print(len(my_list3))

#Para adicionar elementos ao final de uma lista, usamos append()
my_list.append("novo elemento")
print(my_list)

#Extrair um valor da lista, deixando vazio, será o último índice, se não, podemos atribuir um índice qualquer
print(my_list.pop()) #Nesta linha, será printado oque foi retirado
print(my_list) #Nesta a lista printada, não terá o último índice, pois foi retirado logo acima
print(my_list.pop(1)) #Retirando por índice
print(my_list)

#Permanentemente inverter uma lista
print(my_list3)
print(my_list3.reverse()) #Não retorna nada, porém a mudança é permanente
print(my_list3)
#Também é possível usar o reverse através de índice
print(my_list3[::-1]) #O retorno será o valor original de my_list3 porque logo antes ela havia sido revertida


#Utilizamos .sort() para ordernar a lista de maneira numérica ou alfabética
my_list4 = ["a", "b", "g", "t", "p", "k", "m", "l"]
print(my_list4.sort()) #Não retorna nada, porém ordena a lista
print(my_list4)

#Podemos criar matrizes com listas também
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
matrix = [lista1, lista2, lista3]
print(matrix)

#Acessando o elemento de uma matriz
print(matrix[1][2])

#Método de compreensão de lista
first_col = [row[0] for row in matrix]
print(first_col)

#É equivalente a:
first_col2 = [matrix[0][0], matrix[1][0], matrix[2][0]]
print(first_col2)
