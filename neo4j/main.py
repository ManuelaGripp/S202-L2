from database import Database
from match_database import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.88.188.235:7687", "neo4j", "digit-endeavors-swimmers")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
match_db = MatchDatabase(db)

# Criando jogadores
match_db.create_player("João","Flamengo" )
match_db.create_player("Mariana", "Vasco")
match_db.create_player("Vitoria", "Vasco")
match_db.create_player("Arthur", "Vasco")


# Criando alguns partidas
match_db.create_match("Flamengo",1)
match_db.create_match("Vasco", 2)
match_db.create_match("Fluminense", 3)
match_db.create_match("Botafogo", 4)

# Ligando jogadores as partidas
match_db.insert_player_in_match("João", 1)
match_db.insert_player_in_match("Mariana", 1)
match_db.insert_player_in_match("Mariana", 2)
match_db.insert_player_in_match("Arthur", 3)
match_db.insert_player_in_match("Arthur", 4)
match_db.insert_player_in_match("Vitoria", 4)
match_db.insert_player_in_match("Vitoria", 1)

# Atualizando o nome de um jogador e atualizando o plcar
match_db.update_player("João", "Pedro")
match_db.update_match("Vasco", "Flamengo")


# Deletando um aluno e uma aula
match_db.delete_match("Pedro")
match_db.delete_match(1)

# Print de todas as informações do banco de dados
print("Matchs:")
print(match_db.get_match())
print("Players:")
print(match_db.get_player())


# Fechando a conexão
db.close()