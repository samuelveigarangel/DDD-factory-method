# Simple Factory
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self: object) -> None:
        pass


class Cachorro(Animal):

    def falar(self):
        print('Au au')


class Gato(Animal):

    def falar(self):
        print('Miau!')


# Fábrica
class Fabrica:

    def criar_animal_falante(self, tipo):
        return eval(tipo)()


# cliente
if __name__ == '__main__':
    fab = Fabrica()
    animal = input('Qual animal vc quer que fale? [Cachorro, Gato] ')
    obj = fab.criar_animal_falante(animal)
    obj.falar()