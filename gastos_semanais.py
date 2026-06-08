# DEFININDO VARIAVEIS
dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
valor_dias_semana = []
total_semanal: float = 0.0
media_semanal: float = 0.0


def lista_menor_valor(lista):
    posicao = 0
    
    for i in lista:
        for j in lista:
            if (i > j):
                posicao = j
    
    return posicao


# COLETANDO GASTOS NA SEMANA
print("\n")
print("============ CALCULADORA DE GASTO SEMANAL - INSERT VALUES ============")

for dias in dias_semana:
    if (dias[-1] == 'a'):
        valor_dias_semana.append(float(input(f"Valor gasto na {dias}: ")))
    elif (dias[-1] == 'o'):
        valor_dias_semana.append(float(input(f"Valor gasto na {dias}: ")))

print("======================================================")
print("\n")


# TOTAL GASTO
total_semanal = sum(valor_dias_semana)


# MÉDIA POR DIA
media_semanal = (total_semanal / 7)


# PEGANDO O DIA COM MENOS GASTOS
dia_menor_gasto_valor: float = 0.0
dia_menor_gasto_posicao: int = 0
dia_menor_gasto: str = ""

dia_menor_gasto_valor = min(valor_dias_semana)
dia_menor_gasto_posicao = valor_dias_semana.index(dia_menor_gasto_valor)
dia_menor_gasto = dias_semana[dia_menor_gasto_posicao]

# PEGANDO O DIA COM MAIS GASTOS
dia_maior_gasto_valor: float = 0.0
dia_maior_gasto_posicao: int = 0
dia_maior_gasto: str = ""

dia_maior_gasto_valor = max(valor_dias_semana)
dia_maior_gasto_posicao = valor_dias_semana.index(dia_maior_gasto_valor)
dia_maior_gasto = dias_semana[dia_maior_gasto_posicao]


# EXIBINDO RESULTADOS
print("=========== RESULTADOS ==========")

print(f"Valor gasto na semana: {total_semanal:.2f} R$")
print(f"Estimativa de gasto por dia: {media_semanal:.2f} R$")
print(f"Dia mais barato: {dia_menor_gasto}, com {dia_menor_gasto_valor} R$")
print(f"Dia mais caro: {dia_maior_gasto}, com {dia_maior_gasto_valor} R$")

print("=================================")
print("\n")
