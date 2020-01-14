# -*- coding: utf-8 -*-
a = 2
b = 0

try:
    print(a/b) #Resultará em um erro, afinal, não é possível dividir por 0 (fora do bloco try/except)
except:
    print("Divisão por 0 não é permitida.")

print("Continuou")