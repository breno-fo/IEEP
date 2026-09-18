import mysql.connector as m

sql = m.connect(
    host = "localhost",
    database = "banda",
    user = "root",
    password = "")

executar = m.cursor()
query = "INSERT INTO musica (id_discos, nome) VALUES (3,ronaldo)"
executar.execute(query)
sql.commit()