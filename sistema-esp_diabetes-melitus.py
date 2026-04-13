# SISTEMA ESPECIALISTA - DETECTOR DE DIABETES MELLITUS
# FONTE DA PESQUISA: https://diretriz.diabetes.org.br/diagnostico-de-diabetes-mellitus/
# ACESSO EM 13/04/2026  


import sys

def motor_inferencia(glic, clas):
    # PACIENTE HIPOGLICEMICO
    if (glic < 70):
        print("O índice glicemico indica hipoglicemia.")

    # NORMAL 
    elif (70 <= glic < 100):
        if (clas == "Alto" or clas == "Muito Alto"):
            print("Realizar teste adicional TTGO.")
        
        else:
            print("Paciente saudável")

    # PRE DIABETES
    elif (100 <= glic <= 125):
        print("Realizar teste adicional TTGO.")
    
    # DIABETES
    elif (glic >= 126):
            print("Realizar teste adicional GJ, HbA1c ou TTGO.")
        

# CLASSIFICACAO NO FINDRISC
def func_findisc(pont):
    if pont < 7:
        return "Baixo"
    elif 7 <= pont <= 11:
        return "Levemente elevado"
    elif 12 <= pont <= 14:
        return "Moderado"
    elif 15 <= pont <= 20:
        return "Alto"
    elif pont >= 20:
        return "Muito alto"


# COLETANDO GLICEMIA
try:
    glicemia = float(input("Digite o nivel de glicemia em jejum (mg/dl) do paciente: "))
except ValueError:
    print("Erro: digite um valor válido!")
    sys.exit()


# INICIALIZANDO SINTOMAS (É ASSUMIDO QUE NÃO HÁ NENHUM)
sintomas = 0


# COLETANDO FINDRISC
pontuacao = int(input("Digite a pontuação total de riscos: "))
classificacao = func_findisc(pontuacao)


# CHAMANDO SISTEMA ESPECIALISTA
print("----- RESULTADO -----")
print(f"Classificacao com base na pontuação apresentada: {classificacao}")
motor_inferencia(glicemia, classificacao)







 
