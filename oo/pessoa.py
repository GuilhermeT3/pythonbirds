class Pessoa:
    olhos = 1

    def __init__(self,*filhos, nome = None, idade = 17):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    
if __name__ == '__main__':
    teles = Pessoa(nome ='Teles')
    guilherme = Pessoa(teles ,nome ='Guilherme')
    print(Pessoa.cumprimentar(guilherme))
    print(id(guilherme))
    print(guilherme.cumprimentar())
    print(guilherme.nome)
    print(guilherme.idade, 'Anos')
    for filho in guilherme.filhos:
        print(filho.nome)
    guilherme.sobrenome = 'Silva'
    print(guilherme.sobrenome)
    del guilherme.filhos
    guilherme.olhos = 1
    del guilherme.olhos
    print(guilherme.__dict__)
    print(teles.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(teles.olhos)
    print(guilherme.olhos)
    print(id(Pessoa.olhos),id(guilherme.olhos), id(teles.olhos))