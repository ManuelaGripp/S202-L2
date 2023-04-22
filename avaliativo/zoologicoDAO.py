from Database import Database


class ZoologicoDAO:

    def __init__(self):
        self.db = Database('S202', 'Animal')

    def createAnimal(self, animal):
        novoAnimal = {
            "id": animal.id,
            "name": animal.nome,
            "especie": animal.especie,
            "idade": animal.idade,
            "habitat": [{
                'id': animal.habitat.id,
                'nome': animal.habitat.nome,
                'tipoAmbiente': animal.habitat.tipoAmbiente,
                'cuidador': {
                    'id': animal.habitat.cuidador.id,
                    'nome': animal.habitat.cuidador.nome,
                    'documento': animal.habitat.cuidador.documento
                }
            }]
        }
        self.db.collection.insert_one(novoAnimal)

    def readAnimal(self, id):
        animal = self.db.collection.find({'id': id})
        return animal

    def upadteAnimal(self, id, nome, idade):
        result = self.db.collection.update_one(
            {"id":id },
            {"$set": {
                "name": nome,
                "idade": idade
            }
            }
        )
        if (result.acknowledged):
            print('Atualizado com sucesso!')
        else:
            print('Erro ao atualizar    !')

    def deleteAnimal(self, id):
        result = self.db.collection.delete_one({'id': id})
        if (result.acknowledged):
            print('Deletado com sucesso!')
        else:
            print('Erro ao deletar!')
