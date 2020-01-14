# -*- coding: utf-8 -*-

#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal
print("Calculadora de dois números e um sinal")
print("Sinais disponíveis:\n+ para soma\n- para subtração\n/ para divisão\n* para multiplicação")

numero1 = input("Digite o primeiro número: ")
numero1_float = float(numero1)
sinal = input("Digite o sinal da operação: ")
numero2 = input("Digite o segundo número: ")
numero2_float = float(numero2)
if sinal == "+":
    resultado = numero1_float + numero2_float
elif sinal == "-":
    resultado = numero1_float - numero2_float
elif sinal == "*":
    resultado = numero1_float * numero2_float
elif sinal == "/":
    resultado = numero1_float / numero2_float
else:
    print("Use apenas os sinais disponíveis")

print("O resultado é: " + str(resultado))