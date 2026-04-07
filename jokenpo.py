import random
import sys

# TITULO
print("======== PEDRA - PAPEL - TESOURA ========")

# INICILIZANDO OPCOES PRO JOGADOR MAQUINA
options = ["Pedra", "Papel", "Tesoura"]
cpu = random.choice(options)

# COLETANDO JOGADA DO USUARIO
user = input("Digite sua jogada (Pedra/Papel/Tesoura): ")
if user not in options:
    print("Digite uma opção válida!")
    sys.exit()

print(f"jogada da máquina: {cpu}")

# RODANDO O JOGO
if user == cpu:
    print("Empate!")
elif ((user == "Pedra" and cpu == "Tesoura") or 
      (user == "Papel" and cpu == "Pedra") or 
      (user == "Tesoura" and cpu == "Papel")):
    print("Ganhou!")
else:
    print("Perdeu!")