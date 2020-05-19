# -*- coding: utf-8 -*-

#Uma função que conseguimos definir com apenas uma linha e tem uma existência temporária, sua validade é apenas sua linha em que foi definida

def square(num):
    """
    Eleva um numero ao quadrado e retorna seu valor
    """ 
    return print(num ** 2)

square(4)

square2 = lambda num: print(num ** 2)
square2(3)

par = lambda x: print(x % 2 == 0)
par(2)

inverter_string = lambda s: print(s[::-1])
inverter_string('Olá, mundo!')