from TableTypes import createTablePokemonTypes,assingPrpertiesToTypes,organizeTypePokemons,pokemonListReturner
from random import randrange
pokemonList = pokemonListReturner()
tableTypes = createTablePokemonTypes()
assingPrpertiesToTypes(tableTypes)
organizeTypePokemons(tableTypes,pokemonList)

def mainProgram():

    typeRequired = input("Wich type of pokemon you want to figth against?")

    typeRequired =  str.upper(typeRequired)
    for x in range(len(tableTypes)) :

        if typeRequired == str.upper(tableTypes[x].name):

            for y in range(6):
                teamType = randrange(0,len(tableTypes[x].debilities))
                teamType = tableTypes[x].debilities[teamType]
                pokemon = randrange(0,len(tableTypes[teamType].pokemonOfThysType))
                pokemon = tableTypes[teamType].pokemonOfThysType[pokemon]
                print(pokemonList[pokemon].name)
    if  input("Try another type?(y/n)" ) == "y" or input("Try another type?(y/n)" )== "Y" :
        mainProgram()

mainProgram()
    
   


        


    