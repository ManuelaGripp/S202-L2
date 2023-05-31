class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc:$ano_nasc, cpf:$cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc , "cpf": cpf}
        result = self.db.execute_query(query, parameters)
        return result

    def read(self, name):
        query = "MATCH (t:Teacher) WHERE t.name = $name RETURN t"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["t"] for result in results]

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        result = self.db.execute_query(query, parameters)
        return result
