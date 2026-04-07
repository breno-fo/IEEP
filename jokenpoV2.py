import random
import sys

# TITULO
print("======== PEDRA - PAPEL - TESOURA - LAGARTO - SPOCK ========")

# INICILIZANDO OPCOES PRO JOGADOR MAQUINA
options = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
cpu = random.choice(options)

# COLETANDO JOGADA DO USUARIO
user = input("Digite sua jogada (Pedra/Papel/Tesoura/Lagarto/Spock): ")
if user not in options:
    print("Digite uma opção válida!")
    sys.exit()
    
print(f"jogada da máquina: {cpu}")

# RODANDO O JOGO
if user == cpu:
    print("Empate!")
elif ((user == "Lagarto" and cpu == "Spock") or (user == "Lagarto" and cpu == "Papel") or 
      (user == "Spock" and cpu == "Pedra") or (user == "Spock" and cpu == "Tesoura") or
      (user == "Pedra" and cpu == "Tesoura") or (user == "Pedra" and cpu == "Lagarto") or 
      (user == "Papel" and cpu == "Spock") or (user == "Papel" and cpu == "Pedra") or 
      (user == "Tesoura" and cpu == "Papel") or (user == "Tesoura" and cpu == "Lagarto")
      ):
    print("Ganhou!")
else:
    print("Perdeu!")