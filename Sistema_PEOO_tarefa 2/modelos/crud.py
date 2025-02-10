from abc import ABC, abstractmethod

class CRUD(ABC):
    def __init__(self):
        self.objetos = []
    
    def inserir(self, obj):
        self.abrir()
        m = 0
        for c in self.objetos:
            if c.get_id() > m:  # Acesse o ID usando o método get_id()
                m = c.get_id()  # Aqui usamos get_id() ao invés de c.id
        obj.set_id(m + 1)  # E aqui usamos set_id() para definir o ID
        self.objetos.append(obj)
        self.salvar()

    def listar_id(self, id):
        self.abrir()
        for c in self.objetos:
            if c.get_id() == id:  # Acesse o ID usando o método get_id()
                return c    
        return None  
    
    def listar(self):
        self.abrir()
        return self.objetos

    def excluir(self, obj):
        c = self.listar_id(obj.get_id())  
        if c != None:
            self.objetos.remove(c)
            self.salvar()

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def salvar(self):
        pass

    @abstractmethod
    def abrir(self):
        pass
