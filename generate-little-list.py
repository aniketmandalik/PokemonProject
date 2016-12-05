from json import loads
from small import results
from PokemonClass import Pokemon

json = loads(results)
pokemons_list = []
for pokemon in json:
    species = json[pokemon]['species']
    types = json[pokemon]['types']
    baseStats = json[pokemon]['baseStats']
    p = Pokemon(species, types, 100, baseStats)
    pokemons_list.append(p)

print(pokemons_list)
