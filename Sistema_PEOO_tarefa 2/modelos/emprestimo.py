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

    def get_data_emprestimo(self):
        return self.__data_emprestimo

    def get_data_devolucao(self):
        return self.__data_devolucao

    # str
    def __str__(self):
        return f"Livro: {self.__idLivro} - Usuário: {self.__idUsuario} - Reserva: {self.__reserva} - Empréstimo: {self.__data_emprestimo} - Devolução: {self.__data_devolucao}"
    
    # to json
    def to_json(self):
        return {
            "id": self.get_id(),
            "idLivro": self.get_idLivro(),
            "idUsuario": self.get_idUsuario(),
            "reserva": self.get_reserva(),
            "data_emprestimo": self.get_data_emprestimo().strftime("%d/%m/%Y %H:%M"),
            "data_devolucao": self.get_data_devolucao().strftime("%d/%m/%Y %H:%M")
        }

# PERSISTÊNCIA (herança CRUD)

class Emprestimos(CRUD):
    def atualizar(self, obj):
        g = self.listar_id(obj.get_id())  
        if g:
            g.set_idLivro(obj.get_idLivro())
            g.set_idUsuario(obj.get_idUsuario())
            g.set_reserva(obj.get_reserva())
            g.__data_emprestimo = obj.get_data_emprestimo()
            g.__data_devolucao = obj.get_data_devolucao()
            self.salvar()
    
    def salvar(self):
        with open("livros.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)
    
    def abrir(self):
        self.objetos = []
        try:
            with open("emprestimo.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:   
                    g = Emprestimo(
                        obj["id"], obj["idLivro"], obj["idUsuario"], obj["reserva"],
                        datetime.strptime(obj["data_emprestimo"], "%d/%m/%Y %H:%M"),
                        datetime.strptime(obj["data_devolucao"], "%d/%m/%Y %H:%M")
                    )
                    self.objetos.append(g)
        except FileNotFoundError:
            pass

