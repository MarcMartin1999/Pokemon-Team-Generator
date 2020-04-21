from Types import PokType
from  Pokemon import PokemonObject
from selenium.webdriver import Firefox
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary,executable_path="C:/geckodriver.exe")
typeNumber = 0

def createTableTypes():
    tableType = []
    driver.get("http://pokemon-index.com/type") 
    typeNumber = driver.find_elements_by_css_selector("table.type-chart > tbody > tr")
    typeNumber = len(typeNumber)-2
    print(typeNumber)
    
    for x in range(typeNumber) :
        pokemonsType = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/table[2]/tbody/tr["+str(x+2)+"]/td[1]").text
        typeAux =  PokType(pokemonsType)
        print(typeAux)
        tableType.append(typeAux)
    
    return tableType


def organizeTypePokemons(pokemon,tableTypes,numOfPokemon):

    if type(pokemon)==PokemonObject:
        
        for x in tablePokemon[0]:
            if x.name == str.upper(pokemon.pokemonType1)  and str.upper(pokemon.pokemonType2):
                x.assignPokemon(numOfPokemon)