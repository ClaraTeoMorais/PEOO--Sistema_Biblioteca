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
        self.__data_emprestimo = self.set_data_emprestimo(data_emprestimo) #O valor passado como data_emprestimo pode ser uma string ou um objeto datetime, se for string ele converte em datetime.
        self.__data_devolucao = self.set_data_devolucao(data_devolucao)

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
        if isinstance(g, bool):
            self.__reserva = g
        else:
            raise ValueError("O valor de reserva deve ser True ou False")

    def get_reserva(self):
        return self.__reserva

    def set_data_emprestimo(self, data):
        if isinstance(data, datetime): #verifica se a data já é um objeto do tipo datetime antes de armazenar na variável self.__data_emprestimo
            self.__data_emprestimo = data
        else:
            self.__data_emprestimo = datetime.strptime(data, "%d/%m/%Y %H:%M")
        return self.__data_emprestimo

    def get_data_emprestimo(self):
        return self.__data_emprestimo

    def set_data_devolucao(self, data):
        if isinstance(data, datetime):
            self.__data_devolucao = data
        else:
            self.__data_devolucao = datetime.strptime(data, "%d/%m/%Y %H:%M")
        return self.__data_devolucao

    def get_data_devolucao(self):
        return self.__data_devolucao

    # str
    def __str__(self):
        return (f"Livro: {self.__idLivro} - {self.__idUsuario} - {self.__reserva} "
                f"- Empréstimo: {self.__data_emprestimo.strftime('%d/%m/%Y %H:%M')} "
                f"- Devolução: {self.__data_devolucao.strftime('%d/%m/%Y %H:%M')}")

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
    objetos = []

    @classmethod
    def atualizar(cls, obj):
        g = cls.listar_id(obj.get_id())
        if g:
            g._Emprestimo__idLivro = obj._Emprestimo__idLivro
            g._Emprestimo__idUsuario = obj._Emprestimo__idUsuario
            g._Emprestimo__reserva = obj._Emprestimo__reserva
            g._Emprestimo__data_emprestimo = obj._Emprestimo__data_emprestimo
            g._Emprestimo__data_devolucao = obj._Emprestimo__data_devolucao 
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("emprestimo.json", mode="w") as arquivo: # O .to_json converte cada dado(), garantindo o formato correto.
            json.dump([obj.to_json() for obj in cls.objetos], arquivo, indent=4) #Adiciona 4 espaços antes de cada nível do JSON para melhorar a formatação

    @classmethod
    def abrir(cls):
        cls.objetos = []  
        try:
            with open("emprestimo.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    if all(k in obj for k in ["id", "idLivro", "idUsuario", "reserva", "data_emprestimo", "data_devolucao"]): #A função all() retorna True se todos os elementos forem verdadeiros 
                        g = Emprestimo(
                            obj["id"], obj["idLivro"], obj["idUsuario"], obj["reserva"],
                            datetime.strptime(obj["data_emprestimo"], "%d/%m/%Y %H:%M"),
                            datetime.strptime(obj["data_devolucao"], "%d/%m/%Y %H:%M")
                        )
                        cls.objetos.append(g)
                    else:
                        print(f"Erro: Objeto inválido no JSON: {obj}")
        except FileNotFoundError:
            print("Arquivo 'emprestimo.json' não encontrado. Criando novo arquivo vazio.")
            with open("emprestimo.json", mode="w") as arquivo:
                json.dump([], arquivo)  # Cria um JSON vazio para evitar futuros erros


