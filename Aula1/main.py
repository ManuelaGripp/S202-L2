
class Animal:
    def __int__(self, nome, cor, idade, especie, som):
        self.nome=nome
        self.cor=cor
        self.idade=int(idade)
        self.especie=especie
        self.som=som

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self, nova_cor):
         self.cor = nova_cor

class Elefante(Animal):
    def __int__(self,nome,cor, idade,especie,som,tamanho):
        self.tamanho = tamanho
        super.__init__(nome, cor, idade, especie, som)

    def mudar(self):
        if(self.especie == 'Africano' and self.idade < 10):
            self.mudar_tamanho('Pequeno')
            self.som = 'Paaah'
        else:
            if(self.especie == 'Africano' and self.idade >= 10):
                self.mudar_tamanho('Grande')
                self.som = "PAHHHHHH"

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def trombar(self):
        print(self.som)



elefante = Elefante()
elefante.nome = input('Entre com o nome do Elefante:')
elefante.idade = int(input('Entre com a idade do Elefante:'))
elefante.especie = input('Entre com a especie do Elefante:')
elefante.cor = input('Entre com a cor do Elefante:')
elefante.tamanho = input('Entre com o tamanho do Elefante:')
elefante.som = input('Entre com o som do Elefante:')

print('tamanho antes verificação' , elefante.tamanho)


print('som incial: ')
elefante.trombar()
elefante.mudar()
print('tamanho após verificação' , elefante.tamanho)
print('som após verificação: ')
elefante.trombar()

