from Pokemon import PokemonObject
from selenium.webdriver import Firefox
from selenium import webdriver

driver = Firefox()
pokemonsOrderByTypes = [[],[]]


def createTableTypes():

    with Firefox() as driver:


        driver.get("https://pokemondb.net/type") 
        pokemonsType = driver.find_elements_by_css_selector("p.text-center>a")
        
        for x in range(len(pokemonsType)):
            pokemonsOrderByTypes[x]=pokemonsType[x].text

        driver.quit

def assingPokemon(pok):
    if type(pok) == PokemonObject:
        i = 0
        for x in pokemonTypes[0]:
            if pok.pokemonType1 == x or pok.pokemonType2 == x:
                    PokemonTypes[i][i]=pok
            i=i+1
