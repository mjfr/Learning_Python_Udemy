# -*- coding: utf-8 -*-

#Em Python é possível "multiplicar" as strings, assim, repetindo o que há dentro delas x vezes.
string_normal = " ABC CBA "
print(string_normal)
print("\n\n")
string_multiplicada = string_normal * 5
print(string_multiplicada)
print("\n\n")

#Podemos retornar partes da string "pulando" x caracteres
string_pula = "Essa string começa normalmente, porém, nem tudo é o que parece"
print(string_pula)
print("\n\n")
print(string_pula[::2])
print("\n\n")
print(string_pula[::5])
print("\n\n")