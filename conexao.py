import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('biblioteca') #conect ao arquivo biblioteca

cursor = conexao.cursor()

# cursor.execute('CREATE TABLE livros (\
#                 id INTEGER PRIMARY KEY,\
#                 titulo VARCHAR(100),\
#                 autor VARCHAR(100),\
#                 editora VARCHAR(50),\
#                 Genero1 VARCHAR(50),\
#                 Genero2 VARCHAR(50),\
#                 Maximo_Renovaçoes INT,\
#                 Exemplares_disponiveis INT)')



# #Criar uma tabela para os usuarios
# conexao.execute('CREATE TABLE Usuarios (\
#                 id INTEGER PRIMARY KEY,\
#                 nome VARCHAR(100),\
#                 telefone VARCHAR(25),\
#                 nacionalidade VARCHAR(30))')

# #criar uma tabela de emprestimo

# conexao.execute('CREATE TABLE Emprestimos (\
#                 id INTEGER PRIMARY KEY,\
#                 id_livro INTEGER,\
#                 id_usuario INTEGER,\
#                 data_emprestimo DATE,\
#                 data_devolucao DATE,\
#                 Estado_do_Exemplar VARCHAR(30),\
#                 FOREIGN KEY(id_livro) REFERENCES livros(id),\
#                 FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')

#popular a tabela livros

# Correção de sintaxe e identação


conexao.execute('INSERT INTO livros(titulo, autor, editora, Genero1, Genero2, Maximo_Renovaçoes, Exemplares_disponiveis) \
                VALUES ("Senhor dos Anéis", "Tolkien", "Editora A", "Ficção", "Ação", 2, 5), \
                ("Manu", "Michael End", "Editora B", "Romance", "Drama", 3, 8), \
                ("Dom Casmurro", "Machado de Assis", "Editora C", "Aventura", "Fantasia", 1, 3)')


# conexao.execute('INSERT INTO  livros(\
#                 titulo,\
#                 autor,\
#                 editora,\
#                 Genero1,\
#                 Genero2,\
#                 Maximo_Renovaçoes,\
#                 Exemplares_disponiveis,\
#                 VALUES("Senhor dos Anéis",\
#                 "Tolkien", "Editora A", "Ficção", "Ação", 2, 5),\
#                 ("Manu", "Michael End", "Editora B", "Romance", "Drama", 3, 8),\
#                 ("Dom Casmurro", "Machado de Assis", "Editora C", "Aventura", "Fantasia", 1, 3)')

#                 ('L', 'Autor 4', 'Editora A', 'Não Ficção', 'História', 2, 6),
#                 ('Livro 5', 'Autor 5', 'Editora B', 'Mistério', 'Suspense', 2, 7),
#                 ('Livro 6', 'Autor 6', 'Editora C', 'Ficção Científica', 'Ação', 3, 4),
#                 ('Livro 7', 'Autor 7', 'Editora A', 'Romance', 'Drama', 1, 10),
#                 ('Livro 8', 'Autor 8', 'Editora B', 'Aventura', 'Fantasia', 2, 5),
#                 ('Livro 9', 'Autor 9', 'Editora C', 'Não Ficção', 'História', 3, 8),
#                 ('Livro 10', 'Autor 10', 'Editora A', 'Mistério', 'Suspense', 1, 3)')
# #popular tabela Usuarios
# cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Elisa","Brasileira","3254872")')


# cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES ("Joao","Brasileiro","3254854"),("Maria","Franca","12345")')

conexao.commit() #envia as informações

conexao.close() #bom deixar para nao dar conflito
