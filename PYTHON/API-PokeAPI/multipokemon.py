import requests as req

pokemons = ['mewtwo','solgaleo']

for pkm in pokemons:
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{pkm}"
    respostas = req.get(endpoint)
    if respostas.status_code == 200:
        vetor_dados = respostas.json()

        id = vetor_dados['id']
        nome = vetor_dados['name']

        print(f"O pokemon {id} se chama {nome}\n")
    else:   
        print(f"O pokemon {pkm} não existe")