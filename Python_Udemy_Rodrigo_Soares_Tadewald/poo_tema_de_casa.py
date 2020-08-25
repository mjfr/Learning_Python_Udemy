# Programação orientada a objetos - Tema de casa

#### Problema 1
#Preencha os métodos da classe Line para aceitar coordenadas como um par de
#tuplas e retornar a inclinação e a distância da linha.

class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return print(((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5) # **0.5 = raiz

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return print(float((y2-y1) / (x2-x1)))

# Output exemplo

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

#### Problema 2
#Preencha a classe
class Cylinder(object):
    pi = 3.14159265359
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return print((self.pi * (self.radius ** 2)) * self.height)
    
    def surface_area(self):
        return print((self.height * (2 * self.pi * self.radius)) + 2 * self.pi * self.radius ** 2)

# Exemplo de saída
c = Cylinder(2,3)
c.volume()
c.surface_area()