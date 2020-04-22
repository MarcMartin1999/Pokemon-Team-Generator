from Types import PokType
from  Pokemon import PokemonObject
from selenium.webdriver import Firefox
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary,executable_path="C:/geckodriver.exe")



def createTablePokemonTypes():
    tableTypePokemons = []
    driver.get("http://pokemon-index.com/type") 
    typeNumber = driver.find_elements_by_css_selector("table.type-chart > tbody > tr")
    typeNumber = len(typeNumber)-2
    
    for x in range(typeNumber) :
        pokemonsType = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/table[2]/tbody/tr["+str(x+2)+"]/td[1]").text
        typeAux =  PokType(pokemonsType)
        tableTypePokemons.append(typeAux)
    


    return tableTypePokemons

def assingPrpertiesToTypes(table):
    driver.get("http://pokemon-index.com/type") 
    typeNumber = driver.find_elements_by_css_selector("table.type-chart > tbody > tr")
    typeNumber = len(typeNumber)-2

    driver.get("https://pokemondb.net/type")
    for y in range(typeNumber) :

        for x in range(typeNumber) :
            
            aux = driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div/table/tbody/tr["+str(y+1)+"]/td["+str(x+1)+"]")
            aux = aux.get_attribute("class")
            
            if aux == "type-fx-cell type-fx-50":
                table[y].debilitiesATK.append(x)
            
            if aux =="type-fx-cell type-fx-0":
                table[y].noDamageTo.append(x)
            
            if aux =="type-fx-cell type-fx-200":
                table[y].strengthATK.append(x)




def organizeTypePokemons(tablePokemon,tableTypes,numOfType):
    
    auxTable = []
        
    for y in range(len(tablePokemon)):

        if str.upper(tablePokemon[y].pokemonType1) ==str.upper(tableTypes[numOfType].name) or str.upper(tablePokemon[y].pokemonType2) ==str.upper(tableTypes[numOfType].name):

            auxTable.append(y)