# -*- coding: utf-8 -*-

#Heranças permitem a reutilização de classes. Fazendo com que classes futuras herdem parâmetros e métodos de classes superiores.

class Animal(object):
    def __init__(self):
        print('Animal created.')

    def whoAmI(self):
        print("I'm an animal.")

    def eat(self):
        print('Eating...')

animal1 = Animal()
animal1.whoAmI()
animal1.eat()


print('\n\n')


#Ao invés de passar o object, passamos a classe que queremos que a nova classe herde
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self) #Criando o construtor da classe Animal
        print('Dog created.')

    def whoAmI(self):
        print("I'm a dog")
    
    def bark(self):
        print('Au au')
    
sam = Dog()
sam.whoAmI()
sam.bark() #Método próprio
sam.eat() #Método herdado