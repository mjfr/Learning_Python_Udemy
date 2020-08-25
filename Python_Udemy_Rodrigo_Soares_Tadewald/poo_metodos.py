# -*- coding: utf-8 -*-
#Métodos são funções internas em classes que podem fazer operações com os atributos

class Dog(object):
    species = 'Mammal'
    def __init__(self, raca):
        self.raca = raca
        self.num_caractere = len(self.species)
    
    #Definindo um método para a classe Dog
    def bark(self):
        print("Au au")

sam = Dog(raca='Labrador')
sam.bark()

class Circle(object):
    pi = 3.1415

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * self.pi
    
    def defRadius(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius

circle = Circle() #Ao colocar um valor entre parênteses, estaríamos sobrescrevendo o valor já existente
print(circle.radius)
print(circle.area())
circle.defRadius(2)
print(circle.area())
print(circle.getRadius())



print('\n\n\n\n\n\n\n')


#Métodos especiais

class Book(object):
    def __init__(self, title, author, pages):
        print('A book was created.')
        self.title = title
        self.author = author
        self.pages = pages
    
    #Habilita a leitura de dados """Traduzindo o endereço de memória para uma versão em String"""
    def __str__(self):
        return "Title {a}".format(a=self.title)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Book destroyed')

book1 = Book('Python', 'Matheus', 100)
print(book1)
print(len(book1))
print(book1.author)
del book1
