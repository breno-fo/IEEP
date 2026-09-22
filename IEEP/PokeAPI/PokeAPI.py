# Importando bibliotecas
import requests
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO

# Criando a janela de exibição
window = Tk()
window.title("PokeAPI - The most cool pokemons ever")

# Pokemons que serão exibidos
pokers = [
    "lechonk", 
    "mewtwo", 
    "pidgey", 
    "pidgeot", 
    "dugtrio",
    "rattata",
    "spearow",
    "butterfree",
    "caterpie",
    "weedle",
    "metapod"
    ]

p_fotos = []

# Laço principal
for cod, p in enumerate(pokers):
    # Processando endpoint
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{p}"
    resposta = requests.get(endpoint)

    # Processando resposta
    if (resposta.status_code == 200):
        # Convertendo o conteúdo em json
        poke_array = resposta.json()

        # Conteúdo do endpoint que será usado
        p_nome = poke_array["name"]
        p_id = poke_array["id"]
        p_img_link = poke_array["sprites"]["front_default"]

        # Baixando a imagem LINK -> PNG
        p_img_download = requests.get(p_img_link)

        if (p_img_download.status_code != 200):
            print("Erro: Nao foi possivel baixar a imagem!")
            p_img_download.content = "Imagem nao processada"
        else:
            linha = cod // 3
            coluna = cod % 3

            img = Image.open(BytesIO(p_img_download.content))
            img = img.resize((120, 120))

            img_tk = ImageTk.PhotoImage(img)
            p_fotos.append(img_tk)

            # Labels (Nome/Id + Foto)
            label_p_nome = Label(window, text=(f"Nome: {p_nome} \nId: {p_id}"))
            label_p_nome.grid(row=(linha*2), column=coluna)

            label_img = Label(window, image=img_tk)
            label_img.grid(row=(linha*2)+1, column=coluna, padx=5)

window.mainloop()



