# mongoimport --db=pokemondb --collection=pokemon_data --type=csv --fields name,pokedex_number,type1,type2,hp,attack,defense,speed,sp_attack,sp_defense,abilities --file pokemon.csv

import sqlite3
from pymongo import MongoClient

# Connect to SQLite database
sqlite_conn = sqlite3.connect('pokemon.sqlite')
sqlite_cur = sqlite_conn.cursor()

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Execute a SELECT query on SQLite
sqlite_query = '''SELECT p.name, p.pokedex_number, p.type1, p.type2, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, p.abilities
                  FROM imported_pokemon_data AS p
                  '''
sqlite_cur.execute(sqlite_query)

# Iterate through each row and add to MongoDB
for row in sqlite_cur.fetchall():
    pokemon = {
        "name": row[0],
        "pokedex_number": int(row[1]),
        "types": [row[2], row[3]], # type1 and type2
        "hp": int(row[4]),
        "attack": int(row[5]),
        "defense": int(row[6]),
        "speed": int(row[7]),
        "sp_attack": int(row[8]),
        "sp_defense": int(row[9]),
        "abilities": [row[10]] 
    }
    pokemonColl.insert_one(pokemon)

for pokemon in pokemonColl.find():
    print(pokemon)
# Close the connections
sqlite_cur.close()
sqlite_conn.close()
mongoClient.close()
