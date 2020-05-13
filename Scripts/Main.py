from TableTypes import createTablePokemonTypes,assingPrpertiesToTypes,organizeTypePokemons,pokemonListReturner
from random import randrange
from selenium.webdriver import Firefox
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary,executable_path="C:/geckodriver.exe")
pokemonList = pokemonListReturner()
tableTypes = createTablePokemonTypes()
assingPrpertiesToTypes(tableTypes)
organizeTypePokemons(tableTypes,pokemonList)

def mainProgram():
    pokemonTeam =  []
    typeRequired = input("Wich type of pokemon you want to figth against?  ")

    typeRequired =  str.upper(typeRequired)
    for x in range(len(tableTypes)) :

        if typeRequired == str.upper(tableTypes[x].name):

            for y in range(6):
                teamType = randrange(0,len(tableTypes[x].debilities))
                teamType = tableTypes[x].debilities[teamType]
                pokemon = randrange(0,len(tableTypes[teamType].pokemonOfThysType))
                pokemon = tableTypes[teamType].pokemonOfThysType[pokemon]
                pokemonTeam.append(pokemonList[pokemon])
            Images =searchImageTeam(pokemonTeam)
            createWeb(pokemonTeam,Images)
            html_file = os.getcwd() + "\\" + "Scripts\\Web\\webTemplate.html"
            browser.get("file:///" + html_file)
                
    if  input("Try another type?(y/n)" ) == "y" or input("Try another type?(y/n)  " )== "Y" :
        mainProgram()


def createWeb(Team,Images):
    html_file = os.getcwd() + "\\" + "Scripts\\Web\\webTemplate.html"
    web = open(html_file, "w")
    web.write('''<!doctype html>

    <html lang="en">
    <head>
    <meta charset="utf-8">

    <title>PokemonTeamGenerator</title>
    <meta name="PokemonTeamGenerator" content="PokemonTeamGenerator">
    <meta name="Marc" >
    

    <link rel="stylesheet" href="styles.css">

    </head>

    <body>
        <div class="container">
            <img class= imageTitle src="Title.png" > </br>

            <div class= "pokemonContainer"> 
                <p class="pokemonName">'''+Team[0].name+'''</p></br>
                <img  src='''+Images[0]+''' class="pokemonImage" >
            </div>
        
            <div class= "pokemonContainer"> 
                <p class="pokemonName">'''+Team[1].name+'''</p></br>
                <img src='''+Images[1]+''' class="pokemonImage" >
            </div>
            <div class= "pokemonContainer"> 
                <p class="pokemonName">'''+Team[2].name+'''</p></br>
                <img src='''+Images[2]+''' class="pokemonImage" >
            </div>
            <div class= "pokemonContainer"> 
                <p class="pokemonName">'''+Team[3].name+'''</p></br>
                <img src='''+Images[3]+''' class="pokemonImage" >
            </div>
            <div class= "pokemonContainer"> 
                <p class="pokemonName">'''+Team[4].name+'''</p></br>
                <img src='''+Images[4]+''' class="pokemonImage" >
            </div>
            <div class= "pokemonContainer"> 
                <p class="pokemonName">'''+Team[5].name+'''</p></br>
                <img src='''+Images[5]+''' class="pokemonImage" >
            </div>
        
        </div>
    </body>
    </html>''')
    web.close()


def searchImageTeam(Team):
    images=[]
    for x in range(6):
        browser.get("https://pokemondb.net/pokedex/"+str.lower(Team[x].name)) 
        images.append(browser.find_element_by_css_selector("div.text-center>p>a>img").get_attribute("src"))
    
    return images
        
mainProgram()
    
   


        


    