from selenium.webdriver import Firefox
from selenium import webdriver
from  Pokemon import PokemonObject
from Types import createTableTypes,assingPokemon

driver = Firefox()



with Firefox() as driver:
   
   driver.get("https://pokemondb.net/pokedex/national") 
   pokemonsName =driver.find_elements_by_class_name("ent-name")
   pokemonsTypeContainer =driver.find_elements_by_class_name("infocard")  
   
   for x in range(len(pokemonsName)):
      
     
      pokemonAuxType = pokemonsTypeContainer[x].find_elements_by_css_selector("small>a")
      
      if len(pokemonAuxType)  == 2:

         type1= pokemonAuxType[1].text
         type2= pokemonAuxType[0].text
         name = pokemonsName[x].text

         pokemonAux = PokemonObject(name,type1,type2)
         assingPokemon(pokemonAux)

      if len(pokemonAuxType)  == 1:

         type1= pokemonAuxType[0].text
         name = pokemonsName[x].text

         pokemonAux = PokemonObject(name,type1)
         assingPokemon(pokemonAux)

         
   driver.quit

createTableTypes()

