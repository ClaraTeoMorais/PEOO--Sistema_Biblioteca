from modelos.usuario import Usuario, Usuarios

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