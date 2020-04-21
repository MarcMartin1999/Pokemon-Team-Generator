class PokType:

    name:" "
    pokemonOfThisType= []


    def __init__(self,name):

        self.name = name

    def assignPokemon(self,a):
        self.pokemonOfThisType.append(a)
        