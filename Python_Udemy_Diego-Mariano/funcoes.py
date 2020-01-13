#-*- coding: utf-8 -*-
"""
Funções permitem modularizar os códigos.
São executados apenas quando chamados.
Funções são definidas pela palavra reservada "def"
Variáveis declaradas dentro de uma função, apenas existem no escopo local (dentro da função), se chamados fora, não serão reconhecidos

def NOME(PARÂMETROS):
    COMANDOS

chamando a função

NOME(ARGUMENTOS)
"""

def Soma(x, y):
    return x + y

mostrar_soma = Soma(1, 4)
print(mostrar_soma)

def Multiplicacao(x, y):
    return x * y

mostrar_multiplicacao = Multiplicacao(2, 4)
print(mostrar_multiplicacao)

#Também é possível chamar funções de forma recursiva.
print(Soma(mostrar_soma, mostrar_multiplicacao))