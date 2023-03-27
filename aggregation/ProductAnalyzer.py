from database import Database
from saveJson import writeAJson



class ProductAnalyzer:
    def total_cliente_B(self):
        db = Database(database="dex", collection="clients")
        db.resetDatabase()
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply":["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$match":{"_id":"B"}}
        ])
        writeAJson(result, "total_cliente_B")
        print("Resultado salvo no arquivo total_cliente_B")
        return

    def menos_vendido(self):
        db = Database(database="dex", collection="clients")
        db.resetDatabase()
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])
        writeAJson(result, "menos_vendido")
        print("Resultado salvo no arquivo menos_vendido")
        return

    def menos_gastou(self):
        db = Database(database="dex", collection="clients")
        db.resetDatabase()
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$project":{"cliente_id":1, "total":{"$sum": {"$multiply":["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group":{"_id":"$_id","cliente":{"$push":"$cliente_id"}, "menor_compra":{"$sum": "$total"} }},
            {"$sort":{"menor_compra":1}},
            {"$limit": 1}
            ])
        writeAJson(result, "menos_gastou")
        return

    def listar_acima_2(self ):
        db = Database(database="dex", collection="clients")
        db.resetDatabase()
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$match":{"total":{"$gt":2}}}
        ])
        writeAJson(result, "listar_acima_2")
        print("Resultado salvo no arquivo listar_acima_2")
        return
