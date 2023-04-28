
#classes padrão

class Usuario:

    def __init__(self, cpf, nome, email, senha, iduser, contatos):
        self._cpf=cpf
        self._nome=nome
        self._email=email
        self._senha=senha
        self._iduser=iduser
        self._contatos=contatos
    
   
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

    def get_iduser(self):
        return self._iduser
    def set_iduser(self, novo_iduser):
        self._iduser = novo_iduser

    def get_contatos(self):
        return self._contatos
    def set_contatos(self, novo_contatos):
        self._contatos = novo_contatos
    
    def __repr__(self):
        return f'CPF: {self._cpf}\nNome: {self._nome}\nEmail: {self._email}\nSenha: {self._senha}\nId usuário: {self._iduser}\nContatos: {self._contatos}'

