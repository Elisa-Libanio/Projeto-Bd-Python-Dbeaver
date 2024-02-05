import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('biblioteca') #conect ao arquivo biblioteca

cursor = conexao.cursor()



cursor.execute('CREATE TABLE livros (\
                id INTEGER PRIMARY KEY,\
                titulo VARCHAR(100),\
                autor VARCHAR(100),\
                editora VARCHAR(50),\
                Genero1 VARCHAR(50),\
                Genero2 VARCHAR(50),\
                Maximo_Renovaçoes INT,\
                Exemplares_disponiveis INT)')




conexao.commit() #envia as informações

conexao.close() #bom deixar para nao dar conflito