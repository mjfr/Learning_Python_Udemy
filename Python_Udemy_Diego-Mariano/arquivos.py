# -*- coding: utf-8 -*-

"""
Abrindo arquivos em Python, é feito através da função open
VARIÁVEL = open(NOME, MODO)

#Modos:
r  somente leitura (é o valor padrão)
w  escrita(caso o arquivo já exista, será apagado e um novo arquivo vazio será criado)
a  leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
r+ leitura e escrita
w+ escrita (o modo w+, assim como o w, apaga o conteúdo anterior do arquivo)
a+ leitura e escrita (abre o arquivo para atualização)

#Lendo arquivos
read()      lê o arquivo inteiro
readline()  lê apenas uma linha
readlines() lê o arquivo e o armazena em uma lista
"""

#Lendo arquivos

arquivo = open("arquivo_teste.txt")

texto_completo = arquivo.read()
print(texto_completo)

linhas = arquivo.readlines()
print(linhas)
for linha in linhas:
    print(linha)

#Criando arquivos
arquivo2 = open("arquivo_teste_2.txt", "w")
arquivo2.write("Esse é o meu arquivo criado pelo Python\n")
arquivo2.close() #Por mais que o Python feche automaticamente os arquivos, é importante a prática, pois evita erros