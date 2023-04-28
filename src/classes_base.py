
#classes padrão

class Usuario:

    def __init__(self, cpf, nome, email, senha, chave, contatos, chave_user):
        self._cpf=cpf
        self._nome=nome
        self._email=email
        self._senha=senha
        self._chave=chave
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

    def get_chave(self):
        return self._chave
    def set_chave(self, novo_chave):
        self._chave = novo_chave

    def get_contatos(self):
        return self._contatos
    def set_contatos(self, novo_contatos):
        self._contatos = novo_contatos

    def get_chave_user(self):
        return self._chave_user
    def set_chave_user(self, novo_chave_user):
        self._chave_user = novo_chave_user

    
    def __repr__(self):
        return f'CPF: {self._cpf}\nNome: {self._nome}\nEmail: {self._email}\nSenha: {self._senha}\nId usuário: {self._chave}\nContatos: {self._contatos}'

