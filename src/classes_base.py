
#classes padrão

class Usuario:

    def __init__(self, cpf, nome, email, senha, contatos, chave_user):
        self._cpf=cpf
        self._nome=nome
        self._email=email
        self._senha=senha
        self._contatos=contatos
        self._chave_user=chave_user
    
   
    def get_cpf(self):
        return self._cpf   
    def set_cpf(self, novo_cpf):
        if novo_cpf <= 11:
            self._cpf = novo_cpf

    def get_nome(self):
        return self._nome  
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_email(self):
        return self._email
    def set_email(self, novo_email):
        self._email = novo_email
    
    def get_senha(self):
        return self._senha
    def set_senha(self, novo_senha):
        self._senha = novo_senha

    def get_contatos(self):
        return self._contatos
    def set_contatos(self, novo_contatos):
        self._contatos = novo_contatos

    def get_chave_user(self):
        return self._chave_user
    def set_chave_user(self, novo_chave_user):
        self._chave_user = novo_chave_user

    
    def __repr__(self):
        return f'CPF: {self._cpf}\nNome: {self._nome}\nEmail: {self._email}\nSenha: {self._senha}\nContatos: {self._contatos}'


class Mensagem:
    def __init__(self, id,usuario_from, usuario_to, mensagem, chave_msg):
        self._id = id
        self._usuario_from = usuario_from
        self._usuario_to = usuario_to
        self._mensagem = mensagem
        self._chave_msg = chave_msg

    def get_id(self):
        return self._id
    def set_id(self, novo_id):
        self._id = novo_id

    def get_usuario_from(self):
        return self._usuario_from
    def set_usuario_from(self, novo_usuario_from):
        self._usuario_from = novo_usuario_from

    def get_usuario_to(self):
        return self._usuario_to
    def set_usuario_to(self, novo_usuario_to):
        self._usuario_to = novo_usuario_to

    def get_mensagem(self):
        return self._mensagem
    def set_mensagem(self, novo_mensagem):
        self._mensagem = novo_mensagem

    def get_chave_msg(self):
        return self._chave_msg
    def set_chave_msg(self, novo_chave_msg):
        self._chave_msg = novo_chave_msg

