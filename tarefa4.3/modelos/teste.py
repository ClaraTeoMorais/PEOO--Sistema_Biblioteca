from emprestimo import Emprestimo, Emprestimos
from genero import Genero, Generos
from livro import Livro, Livros
from usuario import Usuario, Usuarios
from datetime import datetime


# EMPRÉSTIMO

a = Emprestimo(1, "O Mulato", "Clara", True, datetime.now(), datetime.strptime("17/02/2025 12:00", "%d/%m/%Y %H:%M"))
Emprestimos.inserir(a)

# b = Emprestimo(1, "O Diário de Anne Frank", False, "Amanda", datetime.now(), datetime.strptime("15/02/2025 12:00", "%d/%m/%Y %H:%M"))
# Emprestimos.atualizar(b)

# c = Emprestimo(1, "", "", False, datetime.now(), datetime.now())
# Emprestimos.excluir(c)

for i in Emprestimos.listar():
   print(i)


# GÊNERO

#d = Genero(1, "Aventura")
#Generos.inserir(d)

#e = Genero(1, "Mistério")
#Generos.atualizar(e)

#f = Genero(1, "")
#Generos.excluir(f)

#for i in Generos.listar():
  #  print(i)


# LIVRO

# g = Livro(1, "Pj", "Rick", "fanatasia", "Intriseca", "2025", "5", "5")
# Livros.inserir(g)

# h = Livro(2, "O Mulato", "Aluísio Azevedo", "Ficção", "Maranhão", "2025", "10", "10")
# Livros.atualizar(h)

# j = Livro(1, "", "", "", "", "", "", "")
# Livros.excluir(j)

# for i in Livros.listar():
#     print(i)


# USUÁRIO

# k = Usuario(1, "Bella", "clbellaara@gmail.com", "123")
# Usuarios.inserir(k)

# l = Usuario(1, "Clara Teodósio", "clara.teodosio@gmail.com", "123")
# Usuarios.atualizar(l)

# m = Usuario(2, "", "", "")
# Usuarios.excluir(m)

# for i in Usuarios.listar():
#     print(i)
