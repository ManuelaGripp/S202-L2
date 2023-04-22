from animal import Animal
from cuidador import Cuidador
from habitat import Habitat
from zoologicoDAO import ZoologicoDAO
from pprint import pprint


class ZoologicoCLI:

    def menu(self):
        print("O que deseja fazer?")
        print("1-Criar um animal")
        print("2 - Ler um animal")
        print("3 - Atualizar o nome do animal")
        print("4 - Deletar um animal")
        option = input('Entre com a sua opcao: ')
        return option

    def createAnimal(self):
        ZooBd = ZoologicoDAO()
        idCuidador = input("Id do cuidador: ")
        nomeCuidador = input("Nome do cuidador: ")
        documentoCuidador = input("Documento do cuidador: ")
        novoCuidador = Cuidador(idCuidador, nomeCuidador, documentoCuidador)

        print(novoCuidador.id, type(novoCuidador))

        idHabitat = input("Id do Habitat: ")
        nomeHabitat = input("Nome do Habitat: ")
        tipoHabitat = input("Tipo do Ambbiente: ")
        novoHabitat = Habitat(idHabitat, nomeHabitat, tipoHabitat, novoCuidador)

        print(novoHabitat.cuidador, type(novoHabitat))

        idAnimal = input("Id do Animal: ")
        nomeAnimal = input("Nome do Animal: ")
        especieAnimal = input("Especie do Animal: ")
        idadeAnimal = input("Idade do Animal: ")
        novoAnimal = Animal(idAnimal, nomeAnimal, especieAnimal, idadeAnimal, novoHabitat)

        ZooBd.createAnimal(novoAnimal)

    def readAnimal(self):
        ZooBd = ZoologicoDAO()
        id = input('Entre com o id: ')
        response = ZooBd.readAnimal(id)
        for aux in response:
            pprint(aux)

    def updateAnimal(self):
        ZooBd = ZoologicoDAO()
        id = input('Entre com o id do animal: ')
        novoNome = input('Entre com o novo nome do animal: ')
        novaIdade = input('Entre com a nova idade do animal: ')
        ZooBd.upadteAnimal(novoNome, novaIdade,id)

    def deleteAnimal(self):
        ZooBd = ZoologicoDAO()
        id = input('Entre com o id para deletar o animal: ')
        ZooBd.deleteAnimal(id)
