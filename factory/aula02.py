from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self: object):
        pass


class SecaoPessoal(Secao):

    def __repr__(self: object) -> str:
        return 'Secão Pessoal'


class SecaoProjeto(Secao):

    def __repr__(self: object) -> str:
        return "Seção Projeto"


class SecaoAlbum(Secao):

    def __repr__(self: object) -> str:
        return "Secão Álbum"


class SecaoPublicacao(Secao):

    def __repr__(self: object) -> str:
        return "Seção Publicação"


class Perfil(metaclass=ABCMeta):

    def __init__(self: object) -> None:
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self: object) -> None:
        pass

    def get_secoes(self: object) -> None:
        return self.secoes

    def add_secao(self: object, secao: object) -> None:
        self.secoes.append(secao)


class Linkedin(Perfil):

    def criar_perfil(self: object) -> None:
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPublicacao())


class Facebook(Perfil):

    def criar_perfil(self: object) -> None:
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())


if __name__ == '__main__':
    rede_social = input(
        'Qual rede social quer criar o perfil ? [Linkedin, Facebook]')

    perfil = eval(rede_social)()

    print(f'Criando o perfil no(a) {type(perfil).__name__}')
    print(f'O perfil tem as seções: {perfil.get_secoes()}')
