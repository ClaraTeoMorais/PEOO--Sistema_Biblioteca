import json
from crud import CRUD

# MODELO

class Emprestimo:
    def __init__(self, id, idLivro, idUsuario, reserva):
        self.__id = id
        self.__idLivro = idLivro
        self.__idUsuario = idUsuario
        self.__reserva = reserva
        #COLOCAR DATA DE EMPRESTIMO E DATA DE DEVOLUÇÃO
    
    # GETs E SETs

    def set_id(self, g):
        self.__id = g
    
    def get_id(self):
        return self.__id

    def set_idLivro(self, g):
        self.__idLivro = g
    
    def get_idLivro(self):
        return self.__idLivro

    def set_idUsuario(self, g):
        self.__idUsuario = g
    
    def get_idUsuario(self):
        return self.__idUsuario
    
    def set_reserva(self, g):
        if isinstance(g, bool):  # Verifica se o valor é booleano
            self.__reserva = g
        else:
            raise ValueError("O valor de reserva deve ser True ou False")
    
    def get_reserva(self):
        return self.__reserva


    # str
    def __str__(self):
        return (f"Livro: {self.__idLivro} - {self.__idUsuario} - {self.__reserva}")


# PERSISTÊNCIA (herança CRUD)

class Emprestimos(CRUD):
    @classmethod
    def atualizar(cls, obj):
        g = cls.listar_id(obj.get_id())
        if g:
            g._Emprestimo__idLivro = obj._Emprestimo__idLivro
            g._Emprestimo__idUsuario = obj._Emprestimo__idUsuario
            g._Emprestimo__reserva = obj._Emprestimo__reserva
            cls.salvar()
    
    @classmethod
    def salvar(cls):
        with open("emprestimo.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("emprestimo.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    # print (obj)
                    g = Emprestimo(obj["_Emprestimo__id"], obj["_Emprestimo__idLivro"], obj["_Emprestimo__idUsuario"], obj["_Emprestimo__reserva"])
                    cls.objetos.append(g)
        except FileNotFoundError:
            pass