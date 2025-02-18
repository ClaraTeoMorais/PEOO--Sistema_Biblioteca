from emprestimo import Emprestimo, Emprestimos
from genero import Genero, Generos
from livro import Livro, Livros
from usuario import Usuario, Usuarios
from datetime import datetime


# EMPRÉSTIMO

a = Emprestimo(1, "PJ", "Amanda", True, datetime.now(), datetime.strptime("20/02/2025 12:00", "%d/%m/%Y %H:%M"))
Emprestimos.inserir(a)

# b = Emprestimo(1, "O Diário de Anne Frank", "Bella Morais", True, datetime.now(), datetime.strptime("18/02/2025 12:00", "%d/%m/%Y %H:%M"))
# Emprestimos.atualizar(b)

# c = Emprestimo(2, "", "", True, datetime.now(), datetime.now())
# Emprestimos.excluir(c)

for i in Emprestimos.listar():
  print(i)


# GÊNERO

# d = Genero(1, "Suspense")
# Generos.inserir(d)

# e = Genero(1, "Mistério")
# Generos.atualizar(e)

# f = Genero(1, "")
# Generos.excluir(f)

# for i in Generos.listar():
#   print(i)


# LIVRO

# g = Livro(1, "Harry Potter", "JK", "fanatasia", "Intriseca", "2025", "5", "5")
# Livros.inserir(g)

# h = Livro(1, "O Mulato", "Aluísio Azevedo", "Ficção", "Maranhão", "2025", "10", "10")
# Livros.atualizar(h)

# j = Livro(1, "", "", "", "", "", "", "")
# Livros.excluir(j)

# for i in Livros.listar():
#   print(i)


# USUÁRIO

# k = Usuario(1, "Amanda", "amandaa@gmail.com", "123")
# Usuarios.inserir(k)

# l = Usuario(2, "Clara Teodósio", "clara.teodosio@gmail.com", "123")
# Usuarios.atualizar(l)

# m = Usuario(1, "", "", "")
# Usuarios.excluir(m)

# for i in Usuarios.listar():
#   print(i)
