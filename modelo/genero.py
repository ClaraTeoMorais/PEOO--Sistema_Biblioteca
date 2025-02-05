import Json

# MODELO

class Genero:
  def __init__(self, id, genero):
    self.__id = id
    self.__genero = genero

  def __str__(self):
    print (f"Gênero: {self.__genero}")


# PERSISTÊNCIA (herança CRUD)

