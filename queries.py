import sqlite3
from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Return all the Pokemon named "Pikachu"
pikachus = pokemonColl.find({"name": "Pikachu"})
for p in pikachus:
    print(p)

# Return all the Pokemon with an attack greater than 150
powerful_pokemons = pokemonColl.find({"attack": {"$gt": 150}})
for pokemon in powerful_pokemons:
    print(pokemon) 

# Return all the Pokemon with an ability of "Overgrow"
overgrow_pokemons = pokemonColl.find({"abilities": {"$regex": "overgrow", "$options": "i"}})
for o in overgrow_pokemons:
    print(o)

