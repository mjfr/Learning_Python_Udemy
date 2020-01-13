#-*- coding: utf-8 -*-
#Strings são declaradas entre áspas ou apóstrofos
print("Hey")
print('Oh')

a = "Diego"
b = "Mariano"

#Concatenar strings
concatenar = a + " " + b 
print(concatenar)

#Saber tamanho de strings (espaços também são contados como caracteres)
tamanho = len(concatenar)
print(tamanho)

#Navegar por índices (lembrando que a contagem começa do 0)
print(a[2])
print(a[2], a[3], a[4])
print(concatenar[0:5]) #imprime do índice inicial até o final    inicial:final

#Métodos em String
#Caixa baixa
print(concatenar.lower())

#Caixa alta
print(concatenar.upper())

#Retirar caracteres especiais ou espaços
concat_strip1 = concatenar + "     "
concat_strip2 = concatenar + "\n\n"
print(concat_strip1 + "Seu tamanho é: ")
print(len(concat_strip1))
print(concat_strip2)
print(concat_strip1.strip() + "Seu tamanho é: ")
print(len(concat_strip1.strip()))
print(concat_strip2.strip())

#Converter uma sequência em uma lista
sequencia = "O rato roeu a roupa do Rei de Roma"
sequencia_convertida = sequencia.split(" ") #separar por espaços
print(sequencia_convertida)
sequencia_convertida2 = sequencia.split("r") #separar por letras (é case sensitive)
print(sequencia_convertida2)

#Encontrar a posição de certo caractere em uma String. Se não houver resultados, o retorno é -1
busca = sequencia.find("Rei")
print(busca)
#Em trechos:
print(sequencia[busca : ])

#Substituição de Strings
substituido = sequencia.replace("Rei", "Plebeu")
print(substituido)