# -*- coding: utf-8 -*-

#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade

maioridade = 18
print("Verificador de maioridade.\nIniciando...")

idade_usuario = input("Digite a sua idade: ")

if not idade_usuario.isnumeric() and idade_usuario.isdecimal:
    print("Digite apenas números inteiros")
else:
    if int(idade_usuario) < maioridade:
        print("Você não atingiu a maioridade")
    else:
        print("Você é um adulto")
