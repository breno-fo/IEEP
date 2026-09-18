import requests as r

endpoint = " https://pokeapi.co/api/v2/pokemon/solgaleo "

resposta = r.get(endpoint)

if resposta.status_code == 200:
    vetor = resposta.json()

    id = vetor['id']
    nome = vetor['name']

    print(f"O pokemon {id} se chama {nome}\n")
else:   
    print("Requisição reprovada ou pokemon não encontrado")