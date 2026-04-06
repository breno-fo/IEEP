# SISTEMA ESPECIALISTA - DETECTOR DE DIABETES MELLITUS
# FONTE DA PESQUISA: https://diretriz.diabetes.org.br/diagnostico-de-diabetes-mellitus/
# ACESSO EM 06/04/2026  


import sys

def motor_inferencia(glic, sintoma):
    # PACIENTE HIPOGLICEMICO
    if (glic < 70):
        print("Pelo teste de Glicemia em Jejum (GJ), o paciente não apresenta riscos de adquirir Diabetes Mellitus, mas o índice glicemico indica hipoglicemia.")

    # NORMAL 
    elif (70 <= glic < 100):
        # PACIENTE COM SINTOMAS
        if (sintoma > 0):
            print("Glicemia em Jejum normal, mas o paciente apresenta sintomas. Recomendação: realizar teste adicional TTGO.")
        
        # PACIENTE SEM SINTOMAS    
        else:
            print("Paciente saudável")

    # PRE DIABETES
    elif (100 <= glic <= 125):
        # PACIENTE COM SINTOMAS
        if (sintoma > 0):
            print("Paciente com alta suspeita de Diabetes Mellitus. Recomendação: realizar teste de TTGO para confirmação.")
            
        # PACIENTE SEM SINTOMAS    
        else:
            print("Paciente pré-diabético. Recomendação: acompanhamento nutriocinal e atividade física.")
    
    # DIABETES
    elif (glic > 125):
        # PACIENTE COM SINTOMAS
        if (sintoma > 0):
            print("Paciente com Diabetes Mellitus. Recomendação: iniciar tratamento médico urgente.")
        # PACIENTE SEM SINTOMAS
        else:
            print("Paciente com alteração na glicose. Recomendação: teste adicional de confirmação, como Glicose em Jejum, TTGO ou HbA1c (preferencialmente o mesmo teste).")


# PERGUNTAS DOS SINTOMAS
perguntas = [  
    "O paciente apresentou Polidipsia (sede excessiva)?",
    "O paciente apresentou Poliúria (urinar em excesso)?",
    "O paciente apresentou Polifagia (fome excessiva)?",
    "O paciente apresentou perda de peso inexplicada?"
]


# COLETANDO GLICEMIA
try:
    glicemia = float(input("Digite o nivel de glicemia em jejum (mg/dl) do paciente: "))
except ValueError:
    print("Erro: digite um valor válido!")
    sys.exit()


# INICIALIZANDO SINTOMAS (É ASSUMIDO QUE NÃO HÁ NENHUM)
sintomas = 0


# COLETANDO SINTOMAS
for p in perguntas:
    resposta = input(f"{p} ")
    if resposta == "s":
        sintomas += 1
    elif resposta != "n":
        print("Caractere digitado é inválido!")
        sys.exit()


# CHAMANDO SISTEMA ESPECIALISTA
print("----- RESULTADO -----")
motor_inferencia(glicemia, sintomas)







 