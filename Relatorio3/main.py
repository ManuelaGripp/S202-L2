from pokedex import Database
from saveJson import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

pokemons = db.collection.find()

def getPokemon_poison_gteSpeed(speed):
    pokemon_gte = db.collection.find({"type": "Poison", "base.Speed": { "$gte": speed }})
    writeAJson(pokemon_gte,"poison_gte65")

def writePokemonByType(type):
    pokemonType = db.collection.find({"type":type})
    writeAJson(pokemonType,"pokemonType")

def writePokemonByName(name):
    pokemonName = db.collection.find({"name.english":name})
    writeAJson(pokemonName,"pokemonName")

def writePokemonByCombinedTypes(type1, type2):
    pokemonTypes = db.collection.find({"$and": [{"type": type1}, {"type": type2}] })
    writeAJson(pokemonTypes,"pokemonTwoTypes")

def writePokemonAttackInterval(attack1, attack2):
     pokemonInterval = db.collection.find({"$and": [{"base.Attack": {"$gte":attack1}}, {"base.Attack":{"$lte":attack2}}]})
     writeAJson(pokemonInterval,"pokemonInterval")



