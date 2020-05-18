# -*- coding: utf-8 -*-

#Condicionais 'if, elif, else'

a = 1
b = 2

if a > b:
    print('{} é maior que {}'.format(a, b))
elif a == b:
    print('{} é igual a {}'.format(a, b))
elif a < b:
    print('{} é menor que {}'.format(a, b))
else:
    print('Algo deu errado')


print('\n\n')

#Controle de fluxo de código 'for'
#O for atua como um iterador no Python. Logo, ele é um iterador que passa por uma sequência (listas, tuplas, sets, etc...)

objeto = [1, 2, 3, 4, 5, 6, 7]

for variavel in objeto:
    print(variavel)

for resultado in objeto:
    if resultado % 2 == 0:
        print(resultado, 'é par.')
    else:
        print (resultado, 'é ímpar.')

#Quando estamos iterando sobre tuplas, temos uma peculiaridade chamada tuple unpacking.
tupla = [(1, 2), (2, 3), (3, 4)]
for t1 in tupla:
    print('Retornando tuplas embaladas', t1)
for (t1, t2) in tupla:
    print('Retornando tuplas desembaladas: ', t1, t2)


print('\n\n')

#Iterando em dicionários
d = {'k1' : 1, 'k2' : 2, 'k3' : 3}
for item in d.keys():
    print('Retornando chave: ', item)
for item in d.values():
    print('Retornando valor: ', item)
for item in d.items():
    print('Retornando com valores separados: ', item)
for (chave, valor) in d.items():
    print('Retornando com tuple unpacking: ', chave, ':', valor)



#While, muito semelhante ao for. Executa enquanto uma variável booleana for true. É um loop.

x = 1
while x <= 10:
    print("O valor de x é:", x)
    x += 1

y = 1
#Podemos utilizar o else na estrutura do while
while y < 10:
    print("O valor de y é:", y)
    y += 1
else:
    print("[ELSE]O valor de y é:", y)


print('\n')

#Break <- uma forma de controlar a estrutura de código
z = 1
lista = []
while True:
    lista += [z]
    z += 1
    print(lista)
    if z > 10:
        break
#Se não houvesse o break, o código iria eventualmente travar o computador, pois nunca seria encerrado, uma vez que o while foi decidido como True para sempre

#Continue <- outra forma de controlar a estrutura de código. Ela ignora sua condição acima e continua para a próxima
ate = 50
numero = 0
while numero < ate:
    numero += 1
    if numero % 2 == 1:
        continue
    if numero % 2 == 0:
        print(numero, 'é par')


print('\n')

#Range() <- criação de listas pré determinadas               range(começo, fim, opicional *de quanto em quanto*)
#Range() é um tipo de objeto gerador. Será guardado na memória mas não será inicializado até necessitar o uso de seu iterador
range1 = range(0, 100, 1)
print(range1)
print(type(range1))
print(list(range1))




#COMPREENSÃO EM LISTAS
x = []
for i in range(0, 30):
    x.append(i)
print(x)

print("\n")

#Podemos simplificar para:
x2 = [j for j in range(0, 30)]
print(x2)

'''No caso, seria:
1- atribuir à variável, a formação da lista
2- atribuir uma variável que será cada item de uma lista
3- iniciar uma estrutura for para gerar a lista
4- declarar o método range para dizer quais os limites da lista
'''

print("\n")

#Também podemos fazer operações com essa forma simplificada
x3 = [k * 2 + 1 for k in range(0, 30)]
print(x3)

print("\n")

#Incluíndo uma condição
x4 = [l for l in range(0, 30) if l % 2 == 0]
print(x4)

print("\n")

#Também funciona com strings
x5 = [letra for letra in 'Matheus']
print(x5)

print("\n")

#Exemplo de conversor de temperatura utilizando compreensão em listas
celsius = [0, 10, 15, 20, 30, 50, 100]
fahrenheit = [(temp * (9/5) + 32) for temp in celsius]
print('°C' + str(celsius))
print('°F' + str(fahrenheit))