#-*- coding: utf-8 -*-
lista1 = [1,2,3,4,5]
lista2 = ["Hello","World","List"]
lista3 = [0, "1", 9.9, True]

print(lista1)
print(lista2)
print(lista3)

#Imprimir por índices
print(lista3[2])

#Laço for para imprimir a lista
for item in lista1:
    print(item)

#Tamanho de uma lista
tamanho = len(lista2)
print(tamanho)

#Inserir itens ao final da lista
lista1.append(245)
print(lista1)

#Saber se algo existe na lista
if 3 in lista1:
    print("3 está na lista")

#Remover elementos de uma lista
print(lista2)
del lista2[2] #Para apagar toda a lista, usar apenas 2 pontos. Ou apagar a partir de certo ponto, deixar o índice e :
print(lista2)

#Criando uma lista em branco
lista_branco = []

#E adicionar elemntos sempre que necessário
lista_branco.append("Adicionado 1")
print(lista_branco)

#Ordenação de listas
lista_desordenada1 = [124, 32, 5, 64, 11, 1, 0, 95, 12345, 44]
lista_desordenada2 = [124, 32, 5, 64, 11, 1, 0, 95, 12345, 44]
print(lista_desordenada1)
lista_desordenada1.sort() #Este método simplesmente altera o que já existe
print(lista_desordenada1)

print("\n\n\n")

print(lista_desordenada2)
lista_ordenada2 = sorted(lista_desordenada2) #Este método retorna uma lista
print(lista_desordenada2)
print(lista_ordenada2)

print("\n\n")

lista_desordenada1.sort(reverse=True) #reverse=True para ordenar a lista de forma decrescente
print(lista_desordenada1)

print("\n\n")

lista2.reverse() #Reverse para inverter a ordem da lista. O primeiro passa a ser o último e vice versa
print(lista2)