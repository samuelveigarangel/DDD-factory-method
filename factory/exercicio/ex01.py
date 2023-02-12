"""

Implemente uma classe Shape que tenha um método abstrato area(). 
Depois, implemente as subclasses Triangle, Square e Circle que herdam de Shape e
implementam o método area() de acordo com as fórmulas adequadas para cada 
forma. Em seguida, crie uma classe ShapeFactory que use o método factory para criar
objetos das subclasses Triangle, Square e Circle de acordo com uma string 
passada como parâmetro.

"""
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self: object) -> None:
        pass

    def __repr__(self: object) -> str:
        return f"{self.__class__.__name__}(area={self.area()})"
    

class Triangle(Shape):

    def area(self: object, base: int, altura: int) -> int:
        return (base*altura)/2
    

class Square(Shape):

    def area(self: object, lado: int) -> int:
        return lado*lado

    
class Circle(Shape):
    
    def area(self: object, raio: int) -> int:
        return 3.14*raio*raio
    

class ShapeFactoryCircle:

    def cal_circle(self: object, raio: int) -> int:
        return Circle().area(raio)


class ShapeFactorySquare:
    def cal_square(self: object, lado: int) -> int:
        return Square().area(lado)


class ShapeFactoryTriangle:
    def cal_triangle(self: object, base: int, altura: int) -> int:
        return Triangle().area(base, altura)
    

if __name__ == '__main__':
    factory_circle = ShapeFactoryCircle()
    print(factory_circle.cal_circle(2))