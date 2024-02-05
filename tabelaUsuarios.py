import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('biblioteca') #conect ao arquivo biblioteca

cursor = conexao.cursor()

#Criar uma tabela para os usuarios
conexao.execute('CREATE TABLE Usuarios (\
                id INTEGER PRIMARY KEY,\
                nome VARCHAR(100),\
                telefone VARCHAR(25),\
                nacionalidade VARCHAR(30))')

conexao.commit() #envia as informações

conexao.close() #bom deixar para nao dar conflito
