# -*- coding: utf-8 -*-

#Modo para apenas um valor
def dobro(x):
    return x*2

valor = 2
print(dobro(valor))

#Caso necessário, para uma lista (vários valores), apenas replicaria e concatenaria a lista
lista_valores = [2, 3, 4, 5, 6]
print(dobro(lista_valores))

print("\n/////////////////////////\n")

#Utilizando a função map que pega cada item de uma lista e aplica uma função a eles:
valores_dobrados = map(dobro, lista_valores)
dobrado_convertido = valores_dobrados
#Método com laço de repetição
for v in valores_dobrados:
    print(v)

print("\n/////////////////////////\n")

#Método com conversão de lista
print(list(dobrado_convertido))  #Por algum motivo bizarro, apenas esse print ou apenas o for podem ser printados. Enquanto um aparece o outro some.