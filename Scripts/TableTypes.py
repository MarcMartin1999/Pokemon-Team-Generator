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
        tableAux =[]
        tableAux2 =[]
        pokemonsType = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/table[2]/tbody/tr["+str(x+2)+"]/td[1]").text
        typeAux =  PokType(pokemonsType,tableAux,tableAux2)
        tableTypePokemons.append(typeAux)
    

    return tableTypePokemons


def assingPrpertiesToTypes(table):
    driver.get("http://pokemon-index.com/type") 
    typeNumber = driver.find_elements_by_css_selector("table.type-chart > tbody > tr")
    typeNumber = len(typeNumber)-2
    driver.get("https://pokemondb.net/type")
    for y in range(typeNumber) :
        
        for x in range(typeNumber) :
            
            aux = driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div/table/tbody/tr["+str(x+1)+"]/td["+str(y+1)+"]")
            aux = aux.get_attribute("class")
                
            if aux == "type-fx-cell type-fx-200":
                    
                table[y].debilities.append(x)





def organizeTypePokemons(tableTypes,tablePokemon):
    
    for x in range(len(tablePokemon))     :
    
        for y in range(len(tableTypes)):

            if str.upper(tablePokemon[x].pokemonType1) ==str.upper(tableTypes[y].name) or str.upper(tablePokemon[x].pokemonType2) ==str.upper(tableTypes[y].name):

                tableTypes[y].pokemonOfThysType.append(x)




def pokemonListReturner():

    

    driver.get("https://pokemondb.net/pokedex/national") 

    pokemonsName = driver.find_elements_by_class_name("ent-name")  
    pokemonsTypeContainer = driver.find_elements_by_class_name("infocard")  
    pokemonList = []


    for x in range(len(pokemonsName)):
            
        
        pokemonAuxType = pokemonsTypeContainer[x].find_elements_by_css_selector("small>a")
            
        if len(pokemonAuxType)  == 2:

            type1= pokemonAuxType[1].text
            type2= pokemonAuxType[0].text
            name = pokemonsName[x].text

            pokemonAux = PokemonObject(name,"pokemonImage",type1,type2)
            pokemonList.append(pokemonAux)  
        
        if len(pokemonAuxType)  == 1:

            type1= pokemonAuxType[0].text
            name = pokemonsName[x].text

            pokemonAux = PokemonObject(name,"pokemonImage",type1)
            pokemonList.append(pokemonAux)



    return pokemonList

