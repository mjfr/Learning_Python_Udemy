#-*- coding: utf-8 -*-

#Blocos são trechos de códigos que dependem de outros trechos para serem executados
#Como o Python funciona por identação, é necessário muita atenção a isso.

a = 1
b = 3

#Condicional if
if a > b:
    print("A variável 'a' é maior")
if a < b:
    print("A variável 'a' é menor")


#Condicional else
if a > b:
    print("A variável a é maior que b")
else:
    print("Entrou na condição senão. Logo, a não é maior que b")

#Condicional elif
#É executado a primeira condicional que for verdadeira
if a == b:
    print("Números iguais")
elif a > b:
    print("a é maior que b")
else:
    print("Números diferentes")