# -*- coding: utf-8 -*-

#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão, escreva reprovado
nota_minima = 6.0
limite_maximo = 10.0
limite_minimo = 0.0
reclamacao = "Digite apenas números de 0 a 10. P.S.: Decimais são separados por pontos."
print("Avaliador letivo\n Iniciando...")
nome_input = input("Qual o seu nome? ")
print(nome_input + ", seja bem vindo a plataforma avaliadora do Colégio XPTO")

nota1 = input("Por favor, insira a sua primeira nota: ")
nota1 = nota1.replace(",", ".")
if nota1.isalpha() or float(nota1) > limite_maximo or float(nota1) < limite_minimo:
    print(reclamacao)
else:
    print("Sua primeira nota é: " + nota1)
    nota2 = input("Por favor, insira a sua segunda nota: ")
    nota2 = nota2.replace(",", ".")
    if nota2.isalpha() or float(nota2) > limite_maximo or float(nota2) < limite_minimo:
        print(reclamacao)
    else:
        print("Sua segunda nota é: " + nota2)

        print("Calculando média...")

        media = (float(nota1) + float(nota2)) / 2
        aprovado = "Parabéns, " + nome_input + ", você foi aprovado com a média de " + str(media)
        reprovado = "Infelizmente, " + nome_input + ", a sua média é: " + str(media) + " e você foi reprovado"

        if media < nota_minima:
            print(reprovado)
        else:
            print(aprovado)