class RepertoireDatabase:
    def __init__(self, database):
        self.db = database

    def createSong(self, nome, minutagem, tom):
        query = "CREATE (m:Musica {nome:$nome, minutagem:$minutagem, tom:$tom}) return m as Node"
        parameters = {"nome": nome, "minutagem": minutagem, "tom":tom}
        results = self.db.execute_query(query, parameters)
        return [result["Node"] for result in results]


    def createRepertoire(self, nome):
        query = "CREATE (r:Repertorio {nome: $nome}) return r as Node"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["Node"] for result in results]


    def createArtist(self, nome, genero):
        query = "CREATE (m:Artista {nome:$nome, genero:$genero}) return m as Node"
        parameters = {"nome": nome, "genero":genero}
        results = self.db.execute_query(query,parameters)
        return [result["Node"] for result in results]


    def getSong(self):
        query = "MATCH (m:Musica) RETURN m.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def getRepertoire(self):
        query = "MATCH (m:Repertorio) RETURN m.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def getArtist(self):
        query = "MATCH (m:Artista) RETURN m.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def deleteSong(self, nome):
        query = "MATCH (m:Musica{nome:$nome}) DETACH DELETE m"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def deleteRepertoire(self, nome):
        query = "MATCH (m:Repertorio{nome:$nome}) DETACH DELETE m"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["nome"] for result in results]

    def deleteArtist(self, nome):
        query = "MATCH (m:Artista{nome:$nome}) DETACH DELETE m"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["nome"] for result in results]

    def updateRepertoireName(self, repertorio, novo_repertorio):
        query = "MATCH (r:Repertorio{nome:$repertorio}) SET r.nome=$novo_repertorio return r as Node"
        parameters = {"novo_repertorio": novo_repertorio, 'repertorio':repertorio}
        results = self.db.execute_query(query,parameters)
        return [result["Node"] for result in results]

    def updateSongsName(self, nome, novo_nome):
        query = "MATCH (r:Musica{nome:$nome}) SET r.nome=$novo_nome return r as Node"
        parameters = {"nome": nome, 'novo_nome':novo_nome}
        results = self.db.execute_query(query,parameters)
        return [result["Node"] for result in results]

    def updateArtistName(self, artista, novo_artista):
        query = "MATCH (r:Artista{nome:$artista}) SET r.nome=$novo_artista return r as Node"
        parameters = {"novo_artista": novo_artista, 'artista': artista}
        results = self.db.execute_query(query,parameters)
        return [result["Node"] for result in results]

    def addSongToRepertoire(self, musica, repertorio):
        query = "MATCH (r:Repertorio{nome:$repertorio}), (m:Musica{nome:$musica}) create (m)-[f:FAZ_PARTE] -> (r) return m,r"
        parameters = {"musica":musica, "repertorio":repertorio}
        results = self.db.execute_query(query, parameters)
        return results

    def addSongToArtist(self, musica, artista):
        query = "MATCH (a:Artista{nome:$artista}), (m:Musica{nome:$musica}) CREATE (a) -[p:PRODUZIU]-> (m) return a,m"
        parameters = {"musica":musica, "artista":artista}
        results = self.db.execute_query(query,parameters)
        return results

    def numberOfSongs(self, repertorio):
        query = "MATCH (r:Repertorio{nome:$repertorio}) <-[f:FAZ_PARTE]- (m:Musica) RETURN count(*) as Quantidade"
        parameters = {"repertorio": repertorio, }
        results = self.db.execute_query(query, parameters)
        return [result["Quantidade"] for result in results]

    def removeFromRepertoire(self, musica, repertorio):
        query = "MATCH (m:Musica{nome:$musica}) -[f:FAZ_PARTE]-> (r:Repertorio{nome:$repertorio}) delete f"
        parameters = {"repertorio": repertorio, "musica":musica }
        results = self.db.execute_query(query, parameters)
        return results

    def showRepertoireSongs(self, repertorio):
        query="MATCH (r:Repertorio{nome:$repertorio}) <-[f:FAZ_PARTE]- (m:Musica) RETURN m.nome as Nome"
        parameters = {"repertorio": repertorio}
        results = self.db.execute_query(query, parameters)
        return [result["Nome"] for result in results]