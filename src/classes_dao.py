import sqlite3
import requests
import xmltodict

from src.classes_base import Usuario

#objeto de acesso a dados - DAO

class UsuarioDAO:
    
    def __init__(self, db_path):
        self.db_path = db_path
    
    def cadastrar_usuario(self, usuario):
            
        conexao = sqlite3.Connection(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        INSERT INTO usuarios (cpf,nome,email,senha,chave,contatos,chave_user) 
        VALUES (?, ?, ?, ?, ?, ?,?)
        """
        
        cursor.execute(comando_sql, \
            (usuario._cpf, usuario._nome, usuario._email, usuario._senha, usuario._chave, usuario._contatos,usuario._chave_user))

        conexao.commit()

        conexao.close()

    def buscar_usuario(self, cpf):

        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM usuarios WHERE cpf = ?
        """
        
        cursor.execute(comando_sql, (cpf, ))

        usuario_tupla = cursor.fetchone()

        conexao.close()

        if usuario_tupla is None:
            return None
        
        usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
            email=usuario_tupla[2], senha=usuario_tupla[3],chave=usuario_tupla[4],contatos=usuario_tupla[5], chave_user=usuario_tupla[6])
            


        return usuario


    def buscar_email(self, email):

        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM usuarios WHERE email = ?
        """
        
        cursor.execute(comando_sql, (email, ))

        usuario_tupla = cursor.fetchone()

        conexao.close()

        if usuario_tupla is None:
            return None
        
        usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
            email=usuario_tupla[2], senha=usuario_tupla[3],chave=usuario_tupla[4],contatos=usuario_tupla[5], chave_user=usuario_tupla[6])
            


        return usuario


    def listar_usuarios(self):
        
        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM usuarios
        """

        cursor.execute(comando_sql)

        usuarios_tuplas = cursor.fetchall()

        cursor.close()

        if len(usuarios_tuplas) == 0:
            return None

        usuarios = []

        for usuario_tupla in usuarios_tuplas:

            usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
                email=usuario_tupla[2], senha=usuario_tupla[3],chave=usuario_tupla[4],contatos=usuario_tupla[5], chave_user=usuario_tupla[6])
            
            usuarios.append(usuario)
        
        return usuarios

    def adicionar_contato(self,usuario_existente,usuario_send):

        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        new_contato = usuario_send.get_email()
        
        contatos = usuario_existente.get_contatos()

        if contatos != "":
            contatos_list = eval(contatos)
        else:
            contatos_list = []
        
        contatos_list.append(new_contato)

        comando_sql_nome = """
        UPDATE usuarios SET contatos = ? WHERE email = ?
        """

        email = usuario_existente.get_email()

        cursor.execute(comando_sql_nome, (str(contatos_list),email))

        conexao.commit()

        conexao.close()

    def buscar_codigo_unico(self, codigo_unico):

            conexao = sqlite3.connect(self.db_path)

            cursor = conexao.cursor()

            comando_sql = """
            SELECT * FROM usuarios WHERE chave_user = ?
            """
            
            cursor.execute(comando_sql, (codigo_unico, ))

            usuario_tupla = cursor.fetchone()

            conexao.close()

            if usuario_tupla is None:
                return None
            
            usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
                email=usuario_tupla[2], senha=usuario_tupla[3],chave=usuario_tupla[4],contatos=usuario_tupla[5], chave_user=usuario_tupla[6])
                


            return usuario
