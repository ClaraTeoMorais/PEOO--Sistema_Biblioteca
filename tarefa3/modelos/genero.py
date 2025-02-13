import json
from crud import CRUD

# MODELO

class Genero:
  def __init__(self, id, genero):
    self.__id = id
    self.__genero = genero

  # GETs E SETs

  def set_id(self, g):
     self.__id = g
    
  def get_id(self):
    return self.__id

  def set_genero(self, g):
    if g != "": 
       self.__genero = g
    else: 
      raise ValueError("O nome do gênero não pode ser vazio")
    
  def get_genero(self):
    return self.__genero

  def __str__(self):
    return (f"Gênero: {self.__genero}")


# PERSISTÊNCIA (herança CRUD)

class Generos(CRUD):
  @classmethod
  def atualizar(cls, obj):
    g = cls.listar_id(obj.get_id())
    if g:
      g._Genero__genero = obj._Genero__genero
      cls.salvar()
  
  @classmethod
  def salvar(cls):
    with open("generos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default = vars)
  
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("generos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          g = Genero(obj["_Genero__id"], obj["_Genero__genero"])
          cls.objetos.append(g)
    except FileNotFoundError:
      pass

# Criando uma instância de Generos
# generos = Generos()

# Agora você pode chamar o método salvar() na instância criada
# generos.salvar()