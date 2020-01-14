# -*- coding: utf-8 -*-

#Dicionários são arrays associativos. Logo, uma chave tem um valor vinculado a si
dicionario1 = {"Matheus" : "Homem", "Maria" : "Mulher", "Goiaba" : "Fruta", "Marcos" : "Homem", "Marta" : "Mulher"} #Não há índices em dicionários. Devem ser chamados por chave

print(dicionario1["Matheus"])
print(dicionario1)

print("\n\n")

#Navegando no dicionário
for chave in dicionario1:
    print("Chave [" + chave + "] : Valor [" + dicionario1[chave] + "]")

print("\n\n")

#Retornando todos os itens do dicionário
for i in dicionario1.items():
    print(i) #Serão exibidos em TUPLAS que são conjuntos de dados, assim como listas, porém são imutáveis

print("\n\n")

#Retornar apenas valores
for j in dicionario1.values():
    print(j)

print("\n\n")

#Retornar apenas chaves
for k in dicionario1.keys():
    print(k)

    