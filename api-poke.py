import requests
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO

janela = Tk()
janela.title("Pokemongo")


def ver_um_pokemon():
    endpoint = "https://pokeapi.co/api/v2/pokemon/squirtle"

    resposta = requests.get(endpoint)

    if (resposta.status_code == 200):
        print("API conectado com sucesso!")
        vetor = resposta.json() 
        print(f"nome do pokemon: {vetor['name']}")
        print(f"ID do pokemon: {vetor['id']}")
    else:
        print(f"pokemon nao existe!")        

def ver_VARIOS_pokemons():
    pokers = ['pikachu', 'charizard', 'squirtle']

    for p in pokers:
        endpoint = f"https://pokeapi.co/api/v2/pokemon/{p}"
        resposta = requests.get(endpoint)

        if (resposta.status_code == 200):
            vetor = resposta.json()
            print(f"nome: {vetor['name']}")
            print(f"peso: {vetor['weight']}")

        else:
            print("Erro: pokemon nao encontrado")


def ver_foto_pokemon():
    pokers = ['blastoise', 'starmie', 'eevee']

    for cod, p in enumerate(pokers):
        endpoint = f"https://pokeapi.co/api/v2/pokemon/{p}"
        resposta = requests.get(endpoint)

        if (resposta.status_code == 200):
            vetor = resposta.json()

            nome = vetor['name']
            link_img = vetor['sprites']['versions']['front_default']

            img = requests.get(img)
            ima = Image.open(BytesIO(img.content))
            im2 = ima.resize(250, 250)

ver_foto_pokemon()


