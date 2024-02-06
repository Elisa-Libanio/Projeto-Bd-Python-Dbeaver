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
cursor.execute('SELECT * FROM Livros WHERE autor= "nome do autor"')

# Verificar o número de cópias disponíveis de um determinado livro
cursor.execute('SELECT Exemplares_disponiveis FROM Livros WHERE titulo="nome do livro"')

#Mostrar os empréstimos em atraso.
cursor.execute('SELECT livros.título, usuários.nome,empréstimos.data_de_empréstimo, empréstimos.data_de_devolução,\
                FROM emprestimos\
                INNER JOIN empréstimos ON livros.id_do_livro = empréstimos.id_do_livro')
#delete remover um autor
cursor.execute('DELETE  FROM Livros WHERE autor ="Paulo Coelho"')
#remover um livro

cursor.execute('DELETE FROM Livros WHERE titulo="SENHOR DOS ANEIS"')
#marcar um livro como devolvido

cursor.execute('UPDATE Livros SET Estado_do_Exemplar = "devolvido" WHERE titulo="SENHOR DOS ANEIS"')

cursor.execute('UPDATE Livros SET Exemplares_disponiveis = Exemplares_disponiveis - 1 WHERE titulo="SENHOR DOS ANEIS"')

conexao.commit()
conexao.close()