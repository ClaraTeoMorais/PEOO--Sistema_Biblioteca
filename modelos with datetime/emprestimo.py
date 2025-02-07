import json
from crud import CRUD
from datetime import datetime

# MODELO

class Emprestimo:
    def __init__(self, id, idLivro, idUsuario, reserva, data_emprestimo, data_devolucao):
        self.__id = id
        self.__idLivro = idLivro
        self.__idUsuario = idUsuario
        self.__reserva = reserva
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
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
        print (f"Livro: {self.__idLivro} - {self.__idUsuario} - {self.__reserva} - {self.__data_emprestimo} - {self.__data_devolucao}")
    
    #to json

    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["idLivro"] = self.idLivro
      dic["idUsuario"] = self.idUsuario
      dic["idreserva"] = self.idreserva
      dic["data_emprestimo"] = self.data_emprestimo.strftime("%d/%m/%Y %H:%M")
      dic["data_devolucao"] = self.data_devolucao.strftime("%d/%m/%Y %H:%M")
      return dic    


# PERSISTÊNCIA (herança CRUD)

class Emprestimos(CRUD):
    def atualizar(cls, obj):
        g = cls.listar_id(obj.id)
        if g:
            g.idLivro = obj.idLivro
            g.idUsuario = obj.idUsuario
            g.reserva = obj.reserva
            g.data_emprestimo = obj.data_emprestimo
            g.data_devolucao = obj.data_devolucao
            cls.salvar()
    
    def salvar(cls):
        with open("emprestimo.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    
    def abrir(cls):
        cls.objetos = []
        try:
                with open("emprestimo.json", mode="r") as arquivo:   # r - read
                    texto = json.load(arquivo)
                    for obj in texto:   
                        g = Emprestimo(obj["__id"], obj["__idLivro"], obj["__idUsuario"], obj["__reserva"], datetime.strptime(obj["data_emprestimo"],"%d/%m/%Y %H:%M"),  datetime.strptime(obj["data_devolucao"], "%d/%m/%Y %H:%M"))
                        cls.objetos.append(g)
        except FileNotFoundError:
            pass