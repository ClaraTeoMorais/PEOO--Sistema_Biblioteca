import json
from crud import CRUD

# MODELO

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    # GETs E SETs

    def set_id(self, g):
        self.__id = g
    
    def get_id(self):
        return self.__id

    def set_nome(self, g):
        if g != "": 
            self.__nome = g
        else: 
            raise ValueError("O nome do usuário não pode ser vazio")
    
    def get_nome(self):
        return self.__nome

    def set_email(self, g):
        if g != "": 
            self.__email = g
        else: 
            raise ValueError("Digite um email")
    
    def get_email(self):
        return self.__email

    def set_senha(self, g):
        if g != "": 
            self.__senha = g
        else: 
            raise ValueError("Digite uma senha")
    
    def get_senha(self):
        return self.__senha

    # str
    
    def __str__(self):
        return (f"{self.__nome} - {self.__email} - {self.__senha}")


# PERSISTÊNCIA (herança CRUD)

class Usuarios(CRUD):
    @classmethod
    def atualizar(cls, obj):
        g = cls.listar_id(obj.get_id())
        if g:
            g._Usuario__nome = obj._Usuario__nome
            g._Usuario__email = obj._Usuario__email
            g._Usuario__senha = obj._Usuario__senha
            cls.salvar()
    
    @classmethod
    def salvar(cls):
        with open("usuarios.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
                with open("usuarios.json", mode="r") as arquivo:   # r - read
                    texto = json.load(arquivo)
                    for obj in texto:   
                        g = Usuario(obj["_Usuario__id"], obj["_Usuario__nome"], obj["_Usuario__email"], obj["_Usuario__senha"])
                        cls.objetos.append(g)
        except FileNotFoundError:
            pass

# Usuarios.salvar()