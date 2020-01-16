# -*- coding: utf-8 -*-

lista1 = [1, 2, 3, 4, 5]
lista2 = ["Letras", "Listas", "Casa", "Elefante", "Dobrão", "Extra"]

#A função zip compactará as duas listas e elas serão concatenadas
for numero, nome in zip(lista1, lista2):
    print(numero, nome)

