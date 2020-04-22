from selenium.webdriver import Firefox
from  Pokemon import PokemonObject
from selenium import webdriver as webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
 

binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary,executable_path="C:/geckodriver.exe")

#CODE

def pokemonListReturner():

   driver.get("https://pokemondb.net/pokedex/national") 

   pokemonsName = driver.find_elements_by_class_name("ent-name")

   pokemonsTypeContainer =driver.find_elements_by_class_name("infocard")  

   pokemonList = []


   for x in range(len(pokemonsName)):
         
      
      pokemonAuxType = pokemonsTypeContainer[x].find_elements_by_css_selector("small>a")
         
      if len(pokemonAuxType)  == 2:

         type1= pokemonAuxType[1].text
         type2= pokemonAuxType[0].text
         name = pokemonsName[x].text

         pokemonAux = PokemonObject(name,type1,type2)
         pokemonList.append(pokemonAux)  
      
      if len(pokemonAuxType)  == 1:

         type1= pokemonAuxType[0].text
         name = pokemonsName[x].text

         pokemonAux = PokemonObject(name,type1)
         pokemonList.append(pokemonAux)

   return pokemonList


         



