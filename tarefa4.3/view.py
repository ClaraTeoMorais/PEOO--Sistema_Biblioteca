from modelos.emprestimo import Emprestimo, Emprestimos
from modelos.genero import Genero, Generos
from modelos.livro import Livro, Livros
from modelos.usuario import Usuario, Usuarios
from datetime import datetime, timedelta

class View:
    def usuario_admin():  # cria o usuário admin
        for u in View.usuario_listar():
            if u.get_email() == "admin": 
                return 
        View.usuario_inserir("Admin", "admin", "1234")

    def usuario_autenticar(email, senha):
        for u in View.usuario_listar():
            if u.get_email() == email and u.get_senha() == senha:
                return {"id" : u.get_id(), "nome" : u.get_nome()}
        return None


    # USUÁRIO 

    def usuario_inserir(nome, email, senha):
        u = Usuario(0, nome, email, senha)
        Usuarios.inserir(u)

    def usuario_listar():
        return Usuarios.listar()    

    def usuario_listar_id(id):
        return Usuarios.listar_id(id)    

    def usuario_atualizar(id, nome, email, senha):
        u = Usuario(id, nome, email, senha)
        Usuarios.atualizar(u)

    def usuario_excluir(id):
        u = Usuario(id, "", "", "")
        Usuarios.excluir(u)    


    # EMPRÉSTIMO 

    def emprestimo_inserir(id_Livro, idUsuario, reserva, data_emprestimo, data_devolucao):
        data_emprestimo = datetime.now()
        data_devolucao = data_emprestimo + timedelta(days=7)

        u = Emprestimo(0, id_Livro, idUsuario, reserva, data_emprestimo, data_devolucao)
        Emprestimos.inserir(u)

    def emprestimo_listar():
        return Emprestimos.listar()    

    def emprestimo_listar_id(id):
        return Emprestimos.listar_id(id)    

    def emprestimo_atualizar(id, idLivro, idUsuario, reserva, data_emprestimo, data_devolucao):
        if isinstance(data_emprestimo, str):  
            data_emprestimo = datetime.strptime(data_emprestimo, "%d/%m/%Y %H:%M")
        if isinstance(data_devolucao, str):
            data_devolucao = datetime.strptime(data_devolucao, "%d/%m/%Y %H:%M")

        u = Emprestimo(id, idLivro, idUsuario, reserva, data_emprestimo, data_devolucao)
        Emprestimos.atualizar(u)

    def emprestimo_excluir(id):
        emprestimo = Emprestimos.listar_id(id)
        if not emprestimo:
            raise ValueError("Empréstimo não encontrado")

        Emprestimos.excluir(emprestimo)



    # GÊNERO 

    def genero_inserir(genero):
        u = Genero(0, genero)
        Generos.inserir(u)

    def genero_listar():
        return Generos.listar()    

    def genero_listar_id(id):
        return Generos.listar_id(id)    

    def genero_atualizar(id, genero):
        u = Genero(id, genero)
        Generos.atualizar(u)

    def genero_excluir(id):
        u = Genero(id, "")
        Generos.excluir(u)    
    
    def genero_pegar_por_nome(nome):
        Generos.get_by_name(nome)


    # LIVRO 

    def livro_inserir(livro, autor, idGenero, editora, ano, quantidade, quantDisponivel):
        u = Livro(0, livro, autor, idGenero, editora, ano, quantidade, quantDisponivel)
        Livros.inserir(u)

    def livro_listar():
        return Livros.listar()    

    def livro_listar_id(id):
        return Livros.listar_id(id)    

    def livro_atualizar(id, livro, autor, idGenero, editora, ano, quantidade, quantDisponivel):
        u = Livro(id, livro, autor, idGenero, editora, ano, quantidade, quantDisponivel)
        Livros.atualizar(u)

    def livro_excluir(id):
        u = Livro(id, "", "", "", "", "", "", "")
        Livros.excluir(u)    