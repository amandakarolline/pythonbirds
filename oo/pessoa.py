class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    #criano do atributo dinâmico, vai aparecer apenas para o objeto luciano
    luciano.sobrenome = 'Ramalho'
    #removendo atributo dinamicamente, vai ser removido apenas do objeto luciano
    del luciano.filhos
    #verificando quais os atributos existem para cada um
    print(luciano.__dict__)
    print(renzo.__dict__)
