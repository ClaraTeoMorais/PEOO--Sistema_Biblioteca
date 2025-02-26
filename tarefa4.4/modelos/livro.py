import json
from .crud import CRUD

# MODELO

class Livro:
    def __init__(self, id, livro, autor, idGenero, editora, ano, quantidade, quantDisponivel):
        self.__id = id
        self.__livro = livro
        self.__autor = autor
        self.__idGenero = idGenero
        self.__editora = editora
        self.__ano = ano
        self.__quantidade = int(quantidade) if str(quantidade).isdigit() else 0
        self.__quantDisponivel = int(quantDisponivel) if str(quantDisponivel).isdigit() else 0


    # GETs E SETs
    #Lembrar de ver como colocar o id genero

    def set_id(self, g):
        self.__id = g
    
    def get_id(self):
        return self.__id

    def set_livro(self, g):
        if g != "": 
            self.__livro = g
        else: 
            raise ValueError("O nome do livro não pode ser vazio")

    def get_id_genero(self):
        return self.__idGenero
    
    def get_livro(self):
        return self.__livro

    def set_autor(self, g):
        if g != "": 
            self.__autor = g
        else: 
            raise ValueError("O nome do autor não pode ser vazio")
    
    def get_autor(self):
        return self.__autor

    def set_editora(self, g):
        if g != "": 
            self.__editora = g
        else: 
            raise ValueError("O nome do editora não pode ser vazio")
    
    def get_editora(self):
        return self.__editora

    def set_ano(self, g):
        if g != "": 
            self.__ano = g
        else: 
            raise ValueError("O ano não pode ser vazio")
    
    def get_ano(self):
        return self.__ano
    
    def set_quantidade(self, g):
        self.__quantidade = g
    
    def get_quantidade(self):
        return self.__quantidade
    
    def set_quantDisponivel(self, g):
        self.__quantDisponivel = g
    
    def get_quantDisponivel(self):
        return self.__quantDisponivel

    def set_genero(self, genero):
        self.__idGenero = genero

    # str
    def __str__(self):
        return (f"Livro: {self.__livro} - {self.__autor} - {self.__idGenero} - {self.__editora} - {self.__ano} - {self.__quantidade} - {self.__quantDisponivel}")


# PERSISTÊNCIA (herança CRUD)

class Livros(CRUD):
    @classmethod
    def atualizar(cls, obj):
        g = cls.listar_id(obj.get_id())
        if g:
            g._Livro__livro = obj._Livro__livro
            g._Livro__autor = obj._Livro__autor
            g._Livro__idGenero = obj._Livro__idGenero
            g._Livro__editora = obj._Livro__editora
            g._Livro__ano = obj._Livro__ano
            g._Livro__quantidade = obj._Livro__quantidade
            g._Livro__quantDisponivel = obj._Livro__quantDisponivel
            cls.salvar()
    
    @classmethod
    def salvar(cls):
        with open("livros.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
                with open("livros.json", mode="r") as arquivo:   # r - read
                    texto = json.load(arquivo)
                    for obj in texto:   
                        g = Livro(obj["_Livro__id"], obj["_Livro__livro"], obj["_Livro__autor"], obj["_Livro__idGenero"], obj["_Livro__editora"], obj["_Livro__ano"], obj["_Livro__quantidade"], obj["_Livro__quantDisponivel"])
                        cls.objetos.append(g)
        except FileNotFoundError:
            pass