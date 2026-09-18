import requests as req
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO 

pokemons = [7,99,45,"Lucario", "Raichu", "Solgaleo" ]

janela = Tk()
janela.title("Trabalho foda")

imagens = []

for cod, pkm in enumerate(pokemons):

    endpoint = f" https://pokeapi.co/api/v2/pokemon/solgaleo "(pkm)
    endpoint = "https://pokeapi.co/api/v2/pokemon/" + pkm
    resposta = req.get(endpoint)


    if resposta.status_code == 200:
        vetor = resposta.json()
        nome_pokemons = vetor['name'].capitalize()
        link_imagens = vetor['sprites']
        ['front_default']
        linha = cod // 3
        coluna = cod % 3
        baixar_img = req.get(link_imagens)

        img = image.open(BytesIO(baixar_img))
        img = img.resize(150.150)

        imagens = ImageTk.PhotoImage(img)
        imagens.append(imagens)

        label_pkm_nome = Label(
            janela, text = nome_pokemons
        )

        label_pkm_nome.grid(
            row = linha * 2,
            column = coluna
            pady = (15.5)
        )

        label_imagem = Label(
            janela, Image = imagens
        )
        
        label_imagem.grid(
            row = linha * 2 + 1,
            
        )
        
    else:
        print("POKEMON NAO ENCONTRADO")

janela.mainloop()