# -*- coding: utf-8 -*-

def primeira_funcao():
    pass

#Para definirmos algo como função, devemos primeiramente usar a palavra def, nomear a função e por fim, colocamos os parênteses que conterão os parâmetros.
#Pass significa que a função simplesmente não fará nada

def chamar_ola_mundo():
    print('Olá Mundo')
#Para chamar a função, chamamos ela por seu nome com os parênteses
chamar_ola_mundo()


#Podemos colocar um docstring (Documentação, explicando a função com três áspas)
#Não é necessário dizer qual o tipo de dado a função receberá
def somar(num1, num2):
    """
    Recebe dois números e retorna a soma deles
    """
    return num1 + num2

somar(3, 4)

print('\n')

def primo(num):
    """
    Método para checar se os números são primos dentro de um intervalo.
    """
    for n in range(2, num):
        if num % n == 0:
            print('Não é primo')
            break
    else:
        print('Primo')

primo(1)

#Também podemos deixar funções dentro de funções