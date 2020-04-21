from Pokemon import PokemonObject
from selenium.webdriver import Firefox
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary,executable_path=r"C:\\geckodriver.exe")




#CODE
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
            if pok.pokemonsOrderByTypes == x or pok.pokemonType2 == x:
                    PokemonTypes[i][i]=pok
            i=i+1
