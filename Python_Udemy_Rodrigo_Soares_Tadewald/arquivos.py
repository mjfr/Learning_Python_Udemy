# -*- coding: utf-8 -*-

#No Python, temos funções próprias que podemos interagir com os mesmos. Porém, para arquivos mais simples.
#no caso de arquivos mais complicados como Excel, PDF, etc. Precisaremos de bibliotecas específicas.

#Podemos colocar uma flag para dizer se o arquivo é apenas leitura 'r' ou aceita escrita também 'w'
my_file = open('texto.txt')

#Lê o que há no arquivo
print(my_file.read())

#Um método para definir onde o cursor está
my_file.seek(0)

#Sempre que executar este código, ele lerá do começo de uma linha até o final dela, a partir da posição atual do cursor.
print(my_file.readline())

#Fechamos o arquivo, pois foi aberto apenas para leitura
my_file.close()

#Abrindo novamente para dessa vez escrever no arquivo
my_file = open('texto.txt', 'w')

my_file.write("Aqui estou escrevendo a partir do Visual Studio Code, usando Python")

#Fechando para finalmente poder abrir o mesmo com a adição

my_file.close()

my_file = open('texto.txt')

print(my_file.read())

my_file.close()

#Podemos notar que a edição apagou as informações anteriores e apenas escreveu a mais recente.
#Para ADICIONAR sem excluir, podemos utilizar a flag 'a'.

my_file = open('texto.txt', 'a')

my_file.write('\nAgora, estou adicionando frases ao invés de excluir')

my_file.close()

my_file = open('texto.txt')

print(my_file.read())

my_file.close()