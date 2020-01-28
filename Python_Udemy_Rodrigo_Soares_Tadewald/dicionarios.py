# -*- coding: utf-8 -*-

#Em quesito de tamanho e armazenamento de dados, é igual a uma lista, a única diferença é a forma de acessar seus dados

myList = [1, 2, 3]
print(myList)
print(myList[2]) #Acesso a lista. Lista é um objeto ordenado

print('\n\n')

myDict = {'chave1' : 1.2, 'chave2' : 'string'}
print(myDict)
print(myDict['chave2']) #Não há sequência em dicionários, logo não é um objeto ordenado

print('\n\n')

#Por ter a mesma propriedade que as listas (guardar diversos tipos de dados), podemos inserir listas e matrizes dentro do dicionário e buscar esses valores
myDict2 = {'chave1' : 1.2, 'chave2' : 'string', 'chave3' : [1, 2, [5, 6, 7]]}
print(myDict2)
print(myDict2['chave3'][2][1]) #2 aqui é o array e 1 é o segundo item do array

print('\n\n')

#Dicionários são mutáveis, logo, podemos mudar seus valores quando bem desejarmos
myDict['chave2'] = 'String alterada'
print(myDict)

print('\n\n')

#É possível criar um dicionário do zero e ir expandindo ele conforme a necessidade
myDict3 = {}
myDict3['key1'] = 'Primeiro item'
myDict3['key2'] = 2
myDict3['key3'] = [1, 2, 3]
print(myDict3)

print('\n\n')

#Dicionários aceitam outros dicionários
myDict4 = myDict3
myDict4['key4'] = myDict
print(myDict4)

print('\n\n')

#Mostrar chaves(keys) e valores(values)
print(myDict4.keys())
print(myDict4.values())
print(myDict4['key4'].keys()) #Chaves do dicionário dentro do dicionário
print(myDict4['key4'].values()) #Valores do dicionário dentro do dicionário

#Retorno de todos os items de um dicionário (em forma de tuplas)
print(myDict4.items())