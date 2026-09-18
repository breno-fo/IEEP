import mysql.connector as sql

conexaobd = sql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "aula_20_08"
)

executar = conexaobd.cursor()

query1 = "USE aula_20_08"
executar.execute(query1)

query = "SELECT * FROM disciplinas"
executar.execute(query)

print("se chegou nessa linha o banco foi consultado")
conexaobd.commit()
executar.close()
conexaobd.close()
