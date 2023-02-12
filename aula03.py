from abc import ABC, abstractclassmethod
from uuid import uuid4


class Pessoa(ABC):
    def __init__(self: object, nome: str, sobrenome: str) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome

    @abstractclassmethod
    def ganhar_dinheiro(self: object) -> None:
        pass


class Aluno(Pessoa):
    def __init__(self: object, nome: str, sobrenome: str) -> None:
        super().__init__(nome, sobrenome)
        self.__matricula = str(uuid4()).split('-')[0].upper()

    def ganhar_dinheiro(self: object) -> None:
        print('Ganhar dinheiro')


aluno1 = Aluno('Samuel', 'Veiga')
print(aluno1.__dict__)
