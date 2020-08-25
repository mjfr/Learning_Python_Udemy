# -*- coding: utf-8 -*-

lista = [1, 2, 3]
print(type(lista))
#Lista é apenas uma instância da classe list na qual foi atribuída seu valor. E dentro dessa instância temos métodos específicos da classe
lista.append(7)
lista.sort()

#Classes podem ser interpretadas simplesmente como tipos de dados
#Criando a própria classe:
class SampleClassLala(object):  #A classe deve apresentar letra inicial maiúscula e seu parâmetro deverá ser object
    pass

#Instanciando uma classe é criar um objeto que terá o tipo da classe criada.
x = SampleClassLala()
print(type(x))

class Dog(object):
    #__init__ é uma função obrigatória ao criar uma classe, na qual seu papel é servir de função inicializadora 
    #Funções de inicializações de classes são chamadas de construtores
    #self como parâmetro de construtor: é para dizer ao Python que estamos nos referindo a essa classe
    species = 'Mammal'
    def __init__(self, raca):
        self.raca = raca #estamos dizendo que o parâmetro raca é pertencente a Dog. O primeiro raca de self.raca refere-se ao parâmetro interno da CLASSE. O segundo raca, refere-se ao parâmetro raca da FUNÇÃO __init__
        self.num_caractere = len(self.species)

sam = Dog(raca='Labrador')
print(type(sam))
print(sam.raca)

frank = Dog('Husky')
frank.raca

print(frank.species)
print(frank.num_caractere)