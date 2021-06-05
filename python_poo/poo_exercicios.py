# Preencha os métodos da classe Line para aceitar coordenadas como um par de tuplas 
# e retornar a inclinação e a distância da linha.


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2 - y1) / (x2 - x1)


coordenada1 = (3, 2)
coordenada2 = (8, 10)
li = Line(coordenada1, coordenada2)
# print(li.distance())
# print(li.slope())


# Preencha a classe pra calcular volume e área
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height * 3.14 * self.radius ** 2
    
    def surface_area(self):
        top = (3.14) * (self.radius) ** 2
        return 2 * top + 2 * 3.14 * self.radius * self.height


ci = Cylinder(2, 3)
# print(ci.volume())
# print(ci.surface_area())
