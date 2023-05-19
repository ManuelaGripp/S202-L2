class MatchDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, team):
        query = "CREATE (:Player {name: $name, team:$team})"
        parameters = {"name": name,"team":team}
        self.db.execute_query(query, parameters)

    def create_match(self, winner,round):
        query = "CREATE (:Match {winner: $winner, round:$round})"
        parameters = {"winner": winner, "round":round}
        self.db.execute_query(query, parameters)

    def get_player(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self):
        query = "MATCH (m:Match) RETURN m.winner AS winner"
        results = self.db.execute_query(query)
        return [result["winner"] for result in results]

    def update_player(self, old_team, new_team):
        query = "MATCH (p:PLayer {old_team: $old_team}) SET p.team = $new_team"
        parameters = {"old_team": old_team, "new_team": new_team}
        self.db.execute_query(query, parameters)

    def update_match(self, old_winner, new_winner):
        query = "MATCH (p:Match {old_winner: $old_winner}) SET p.winner = $new_winner"
        parameters = {"old_winner": old_winner, "new_winner": new_winner}
        self.db.execute_query(query, parameters)

    def insert_player_in_match(self, player_name, round_match):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {round: $around_match}) CREATE (p)-[:PLAY]->(m)"
        parameters = {"player_name": player_name, "round_match": round_match}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, round):
        query = "MATCH (m:Match {round: $round}) DETACH DELETE m"
        parameters = {"round": round}
        self.db.execute_query(query, parameters)
