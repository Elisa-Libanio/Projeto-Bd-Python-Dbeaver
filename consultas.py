import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('biblioteca') #conect ao arquivo biblioteca

cursor = conexao.cursor()

# - Listar todos os livros disponíveis
cursor.execute('SELECT * FROM Livros')

# Encontrar todos os livros emprestados no momento

dados = cursor.execute('SELECT Estado_do_Exemplar FROM Emprestimos WHERE Estado_do_Exemplar = "emprestado"')

for livros in dados:
    print(livros)

# Localizar os livros escritos por um autor específico

# Verificar o número de cópias disponíveis de um determinado livro

#Mostrar os empréstimos em atraso.

conexao.commit()
conexao.close()