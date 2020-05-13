# -*- coding: utf-8 -*-

#Podemos pular linhas com \n dentro da string
#Podemos inserir tabulações com \t dentro da string

#Site sobre formatação para Python: https://pyformat.info/

print("This is a string")

#substituição por parâmetros (s)
s = "Substituído!"
print("Essa string '%s' não estava aqui" %(s))

#substituição por parâmetros (r)
dafas = 53114
print("Essa string '%r' não estava aqui" %(dafas))

#R usa repr() e S usa str()

#Podemos imprimir pontos flutuantes em strings dessa forma: %casas_antes.casas_depoisf
print("Imprimindo pontos flutuantes em string! %1.2f" %(13.144))

#Substituíndo mais de um valor
a1 = "String"
a2 = 1234
print("Temos uma %s aqui. Temos um inteiro aqui: %r" %(a1, a2))

#Método format() <-> Tudo que estiver dentro das chaves, estaremos criando um dicionário cujos valores serão substituídos pelos argumentos do format
string1 = "One: {a}, Two: {b}, Three: {c}".format(a=1, b="two dois", c=12.3)
print(string1)