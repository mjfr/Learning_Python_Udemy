# -*- coding: utf-8 -*-

#Em Python é possível "multiplicar" as strings, assim, repetindo o que há dentro delas x vezes.
string_normal = " ABC CBA "
print(string_normal)
print("\n\n")
string_multiplicada = string_normal * 5
print(string_multiplicada)
print("\n\n")


#Indexação

#Podemos retornar partes da string "pulando" x caracteres
#Dois pontos para indexar com frequência
string_pula = "Essa string começa normalmente, porém, nem tudo é o que parece"
print(string_pula)
print("\n\n")
print(string_pula[::2])
print("\n\n")
print(string_pula[::5])
print("\n\n")

#Também podemos começar de uma certa parte, ir até certa parte ou ambas opções.
print(string_pula[8:])
print("\n\n")
print(string_pula[:15])
print("\n\n")
print(string_pula[6:22])
print("\n\n")

#A indexação entende números negativos como a string começando do fim, direita para esquerda
#Lembrando que como não existe zero negativo, o início da string é contabilizado a partir do -1
print(string_pula[-2])
print("\n\n")
print(string_pula[33:-2])
print("\n\n")
print(string_pula[-10:-3])
print("\n\n")

#Strings são imutáveis, logo, não é possível utilizar indexação para alterar elementos individuais de strings
#Porém, podemos concatenar strings
string_concatenada = string_pula + " [CONCATENANDO] " + string_pula
print(string_concatenada)
print("\n\n")

#Também podemos deixar todas as letras de uma string em caixa alta ou caixa baixa
print(string_pula.upper())
print("\n\n")
print(string_pula.lower())
print("\n\n")