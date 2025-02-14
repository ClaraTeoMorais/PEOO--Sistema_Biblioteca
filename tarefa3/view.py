# from modelos.emprestimo import Emprestimo, Emprestimos
# from modelos.genero import Genero, Generos
# from modelos.livro import Livro, Livros
from modelos.usuario import Usuario, Usuarios
# from datetime import datetime, timedelta

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

    # def cliente_listar_id(id):
    #     return Clientes.listar_id(id)    

    # def cliente_atualizar(id, nome, email, senha):
    #     c = Cliente(id, nome, email, senha)
    #     Clientes.atualizar(c)

    # def cliente_excluir(id):
    #     c = Cliente(id, "", "", "", "")
    #     Clientes.excluir(c)    


    # def profissional_inserir(nome, especialidade, conselho):
    #     c = Profissional(0, nome, especialidade, conselho)
    #     Profissionais.inserir(c)

    # def profissional_listar():
    #     return Profissionais.listar()    

    # def profissional_listar_id(id):
    #     return Profissionais.listar_id(id)    

    # def profissional_atualizar(id, nome, especialidade, conselho):
    #     c = Profissional(id, nome, especialidade, conselho)
    #     Profissionais.atualizar(c)

    # def profissional_excluir(id):
    #     c = Profissional(id, "", "", "")
    #     Profissionais.excluir(c) 




    # def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
    #     c = Horario(0, data)
    #     c.confirmado = confirmado
    #     c.id_cliente = id_cliente
    #     c.id_servico = id_servico
    #     c.id_profissional = id_profissional
    #     Horarios.inserir(c)

    # def horario_listar():
    #     return Horarios.listar()    

    # def horario_listar_disponiveis():
    #     horarios = View.horario_listar()
    #     disponiveis = []
    #     for h in horarios:
    #         if h.data >= datetime.now() and h.id_cliente == None: disponiveis.append(h)
    #     return disponiveis   

    # def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
    #     c = Horario(id, data)
    #     c.confirmado = confirmado
    #     c.id_cliente = id_cliente
    #     c.id_servico = id_servico
    #     c.id_profissional = id_profissional
    #     Horarios.atualizar(c)

    # def horario_excluir(id):
    #     c = Horario(id, None)
    #     Horarios.excluir(c)    

    # def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
    #     #data = "05/11/2024"
    #     #inicio = "08:00"
    #     #fim = "12:00"
    #     #intervalo = 60
    #     i = data + " " + hora_inicio   # "05/11/2024 08:00"
    #     f = data + " " + hora_fim      # "05/11/2024 12:00"
    #     d = timedelta(minutes=intervalo)
    #     di = datetime.strptime(i, "%d/%m/%Y %H:%M")
    #     df = datetime.strptime(f, "%d/%m/%Y %H:%M")
    #     x = di
    #     while x <= df:
    #         #cadastrar o horário x
    #         View.horario_inserir(x, False, None, None, None)
    #         #passar para o próximo horário
    #         x = x + d

    # def servico_inserir(descricao, valor, duracao):
    #     c = Servico(0, descricao, valor, duracao)
    #     Servicos.inserir(c)

    # def servico_listar():
    #     return Servicos.listar()    

    # def servico_listar_id(id):
    #     return Servicos.listar_id(id)    

    # def servico_atualizar(id, descricao, valor, duracao):
    #     c = Servico(id, descricao, valor, duracao)
    #     Servicos.atualizar(c)

    # def servico_excluir(id):
    #     c = Servico(id, "", 0, 0)
    #     Servicos.excluir(c)    