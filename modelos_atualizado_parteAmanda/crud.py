from abc import ABC, abstractmethod

class CRUD(ABC):
    def __init__(self):
        self.objetos = []
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.get_id() > m: 
                m = c.get_id()
        obj.set_id(m + 1)  
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.objetos:
            if c.get_id() == id: 
                return c    
        return None  
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c != None:
            cls.objetos.remove(c)
            cls.salvar()

    # Classes abstratas
    
    @classmethod
    @abstractmethod
    def atualizar(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass