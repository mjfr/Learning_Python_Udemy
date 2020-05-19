# -*- coding: utf-8 -*-

"""
Escopo: "Quais variáveis são visíveis para qual parte do código"
Há quatro tipos de escopos (em ordem de prioridade):
1- Local : Vivem em algum contexto pré-especificado do Python. Geralmente dentro de uma função. X é local dentro da referência 'algo()'
    def algo():
        x = 1
        return x
2- Enclosing functions : Nome no escopo local de todas e quaisquer funções encapsuladas (def ou lambda), de dentro apra fora. Funções dentro de funções
3- Global : Nomes atribuídos no nível superior de um arquivo de módulo, ou declarados como global em uma def dentro do arquivo. X = 9 é global
x = 9    
    def algo():
        x = 1
        return x
4- Built-in : Nomes pré-atribuídos no módulo: open, range, SyntaxError, ...
"""

#x é local:
f = lambda x: x**2

#2º name, dentro de greet() é enclosing function
name = 'This is a global name'
def greet():
    name = 'Sammy'
    def hello():
        print("Hello " + name)
    hello()
#Nesse caso, como não há name dentro de hello(), ele passará a procurar por name dentro de greet()
greet()

#Name é global
#O name que está fora da função greet(), não participa de nenhuma outra função, logo ele é global
print(name)

#Declaração global
"""
Se desejar atribuir um valor a um nome definido no nível superior do programa (fora do escopo de funções/classes), dizemos ao Python
que a variável não é mais local e sim global. Sem fazer desta forma, é impossível atribuir valores a variáveis definidas fora de uma função
"""
numero = 50
def func():
    global numero 
    print('Esta função agora está usando a global numero!')
    print('Por causa do global, o número é: ' + str(numero))
    numero = 2
    print('Rodou func(), mudou a global para: ' + str(numero))
print('Antes de chamar func(), número = ' + str(numero))
func()
print('Depois de chamar a func(), número é: ' + str(numero))