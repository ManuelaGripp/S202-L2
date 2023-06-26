from database import Database
from repertoire_database import RepertoireDatabase

db = Database("bolt://52.204.219.5:7687", "neo4j", "calculation-accidents-transmittal")

repertoire_db = RepertoireDatabase(db)

flag = True

while flag:
    print('O que deseja fazer?')
    print('1 - Adicionar um repertório')
    print('2 - Adicionar uma música')
    print('3 - Adicionar um artista')
    print('4 - Relacionar uma música em um artista')
    print('5 - Adicionar uma música no repertório')
    print('6 - Remover um música do repertório')
    print('7 - Deletar uma música')
    print('8 - Deletar um repertório')
    print('9 - Deletar um artista')
    print('10 - Quantidade de músicas de um repertório')
    print('11 - Saber as músicas de um repertório')
    print('12 - Editar o nome de um repertório')
    print('13 - Editar o nome de uma música')
    print('14 - Editar o nome de um artista')
    print('15 - Encerrar')
    opcao = input('')

    if opcao == '1':
        nome = input('Nome do repertório:')
        node = repertoire_db.createRepertoire(nome)[0]
        print('Repertorio criado com sucesso')
        print('Label: ', node._labels )
        print('Propriedade: ', node._properties )

    elif opcao == '2':
        nome = input('Nome da musica:')
        minutagem = input('Minutagem:')
        tom = input('Tom da musica:')
        node = repertoire_db.createSong(nome, minutagem, tom )[0]
        print('Música criada com sucesso')
        print('Label: ', node._labels )
        print('Propriedade: ', node._properties )

    elif opcao == '3':
        nome = input('Nome do Artista:')
        genero = input('Genero do Artista:')
        node = repertoire_db.createArtist(nome, genero)[0]
        print('Artista criado com sucesso')
        print('Label: ', node._labels )
        print('Propriedade: ', node._properties )

    elif opcao == '4':
        musica = input('Nome da música:')
        artista = input('Nome do artista:')
        repertoire_db.addSongToArtist(musica,artista)
        print('Relacionamento criado com sucesso')

    elif opcao == '5':
        repertorio = input('Nome da repertório:')
        musica = input('Nome da música:')
        repertoire_db.addSongToRepertoire(musica, repertorio)
        print('Música adicionada com sucesso')

    elif opcao == '6':
        musica = input('Nome da música:')
        repertorio = input('Nome do repertório:')
        repertoire_db.removeFromRepertoire(musica, repertorio)
        print('Música removida com sucesso')

    elif opcao == '7':
        musica = input('Nome da música:')
        print(repertoire_db.deleteSong(musica))
        print('Música deletada com sucesso')

    elif opcao == '8':
        repertorio = input('Nome do repertório:')
        repertoire_db.deleteRepertoire(repertorio)
        print('Repertório adicionado com sucesso')

    elif opcao == '9':
        artista = input('Nome do artista:')
        repertoire_db.deleteArtist(artista)
        print('Repertório adicionado com sucesso')

    elif opcao == '10':
        repertorio = input('Nome do repertório:')
        print('Quantidade de músicas: ',repertoire_db.numberOfSongs(repertorio)[0])

    elif opcao == '11':
        repertorio = input('Nome do repertório:')
        musicas = repertoire_db.showRepertoireSongs(repertorio)
        for index,musica in enumerate(musicas):
            print(f'{index+1} - {musica}')

    elif opcao == '12':
        repertorio = input('Nome do repertório:')
        novo_repertorio = input('Novo nome do repertorio:')
        print('Atualizado com sucesso')
        print(repertoire_db.updateRepertoireName(repertorio, novo_repertorio)[0]._properties)

    elif opcao == '13':
        musica = input('Nome da música:')
        nova_musica = input('Novo nome da música:')
        print('Atualizada com sucesso')
        print(repertoire_db.updateSongsName(musica, nova_musica)[0]._properties)
    elif opcao == '14':
        artista = input('Nome do artista:')
        novo_artista = input('Novo nome do artista:')
        print('Atualizado com sucesso')
        print(repertoire_db.updateArtistName(artista, novo_artista)[0]._properties)
    elif opcao == '15':
        flag = False
    else:
        print('Escolha Inválida')




# Fechando a conexão
db.close()