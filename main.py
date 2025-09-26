# Criar um banco de dados SQlite e uma tabela
import sqlite3

# Criar a conexão com o banco de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

# Criar o objeto chamado de "cursor" que será usado para executar os comandos sql
cursor = conexao.cursor()

# # Criar uma tabela no banco
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso TEXT
#     )
# """)
# nome = input("Digite o nome do aluno(a): ").lower()
# idade = int(input(f"Digite a idade do aluno {nome}: "))
# curso = input(f"Digite o curso do aluno {nome}: ").lower()



# Inserir vários alunos de uma vez 
# alunos = [
#     ("Yago", 28, "Direito"),
#     ("Jessica", 24, "Computação"),
#     ("Breno", 28, "Computaria"),
# ]

# # Inserir um dado na tabela - executemany serve para add vairos
# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)
# """,

# (alunos)
# )

# #Confirmar as alterações no banco
# conexao.commit()


#atualizar dados no banco
# cursor.execute("""
# UPDATE alunos
# SET idade = ?, curso = ?
# WHERE id = ?
# """,(61, "Medicina", 3)
# )
# conexao.commit()

#função listar dados no banco 
# cursor.execute("SELECT * FROM alunos")
# for linha in cursor.fetchall(): #consegue trazer todas as linhas da consulta
#     print(f"Id: {linha[0]} | Nome: {linha[1]} | Idade: {linha[2]} | Curso: {linha[3]}")
# print("-" * 50)

# pesquisar = input("Digite o curso que seja pesquisar os alunos: ")
# cursor.execute("SELECT nome, idade FROM alunos WHERE curso = ?", (pesquisar,))
# print(f"Alunos do curso de {pesquisar}")
# for linha in cursor.fetchall():
#     print(f"Nome: {linha[0]} | Idade: {linha[1]}")

# Deletar dados do banco
cursor.execute("DELETE FROM alunos WHERE id = ?", (1,))
conexao.commit()
#Sempre fechar a conexão com o banco de dados
conexao.close()