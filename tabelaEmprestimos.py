import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('biblioteca') #conect ao arquivo biblioteca

cursor = conexao.cursor()


conexao.execute('CREATE TABLE Emprestimos (\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo DATE,\
                data_devolucao DATE,\
                Estado_do_Exemplar VARCHAR(30),\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')


conexao.commit() #envia as informações

conexao.close() #bom deixar para nao dar conflito