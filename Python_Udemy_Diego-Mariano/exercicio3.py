import math
# -*- coding: utf-8 -*-

#Escreva um programa que resolva uma equação de segundo grau
print("Calculadora básica de equações do segundo grau")

#Declarando variáveis
principal_str = input("Digite o coeficiente principal: ")
principal = int(principal_str)
secundario_str = input("Digite o coeficiente secundário: ")
secundario = int(secundario_str)
independente_str = input("Digite o coeficiente independente: ")
independente = int(independente_str)
delta = (math.pow(secundario, 2)) - (4 * principal * independente)
raiz_delta = math.sqrt(delta)
if delta >= 0:
    #Início da conta
    raiz_positiva = (-(secundario) + raiz_delta)  / (2 * principal)
    raiz_negativa = (-(secundario) - raiz_delta)  / (2 * principal)
    print(raiz_positiva)
    print(raiz_negativa)
else:
    print("Delta é menor que zero. Não admite solução no conjunto dos reais")
