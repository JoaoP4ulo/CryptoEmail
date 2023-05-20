import sqlite3
import requests
import xmltodict

from src.classes_base import Usuario, Mensagem

#objeto de acesso a dados - DAO

class UsuarioDAO:
    
    def __init__(self, db_path):
        self.db_path = db_path
    
    def cadastrar_usuario(self, usuario):
        try:        
            conexao = sqlite3.Connection(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
            INSERT INTO usuarios (cpf,nome,email,senha,contatos,chave_user) 
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(comando_sql, \
                (usuario._cpf, usuario._nome, usuario._email, usuario._senha, usuario._contatos,usuario._chave_user))
            conexao.commit()
        except sqlite3.Error as error:
            print("Erro ao deletar mensagem:", error)
        finally:
            if conexao:
                conexao.close()

    def buscar_usuario(self, cpf):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
            SELECT * FROM usuarios WHERE cpf = ?
            """
            cursor.execute(comando_sql, (cpf, ))
            usuario_tupla = cursor.fetchone()

            if usuario_tupla is None:
                return None
            
            usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
                email=usuario_tupla[2], senha=usuario_tupla[3],contatos=usuario_tupla[4], chave_user=usuario_tupla[5])
                
            return usuario
        except sqlite3.Error as error:
            print("Erro ao buscar usuario:", error)
        finally:
            if conexao:
                conexao.close()


    def buscar_email(self, email):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
            SELECT * FROM usuarios WHERE email = ?
            """   
            cursor.execute(comando_sql, (email, ))
            usuario_tupla = cursor.fetchone()
            if usuario_tupla is None:
                return None
            
            usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
                email=usuario_tupla[2], senha=usuario_tupla[3],contatos=usuario_tupla[4], chave_user=usuario_tupla[5])
            
            return usuario
        except sqlite3.Error as error:
            print("Erro ao buscar email:", error)
        finally:
            if conexao:
                conexao.close()


    def listar_usuarios(self):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
            SELECT * FROM usuarios
            """
            cursor.execute(comando_sql)
            usuarios_tuplas = cursor.fetchall()

            if len(usuarios_tuplas) == 0:
                return None

            usuarios = []

            for usuario_tupla in usuarios_tuplas:

                usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
                    email=usuario_tupla[2], senha=usuario_tupla[3],contatos=usuario_tupla[4], chave_user=usuario_tupla[5])
                
                usuarios.append(usuario)
            
            return usuarios
        except sqlite3.Error as error:
            print("Erro ao listar usuarios:", error)
        finally:
            if conexao:
                conexao.close()

    def adicionar_contato(self,usuario_existente,usuario_send):
        try:
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
        except sqlite3.Error as error:
            print("Erro ao adicionar contato:", error)
        finally:
            if conexao:
                conexao.close()



    def buscar_codigo_unico(self, codigo_unico):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
            SELECT * FROM usuarios WHERE chave_user = ?
            """
            cursor.execute(comando_sql, (codigo_unico, ))
            usuario_tupla = cursor.fetchone()

            if usuario_tupla is None:
                return None
            
            usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
                email=usuario_tupla[2], senha=usuario_tupla[3],contatos=usuario_tupla[4], chave_user=usuario_tupla[5])

            return usuario
        except sqlite3.Error as error:
            print("Erro ao buscar codigo unico:", error)
        finally:
            if conexao:
                conexao.close()

class MensagemDao:

    def __init__(self,db_path):
        self.db_path = db_path

    def buscar_id(self, mensagem_id):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
                SELECT * FROM mensagens WHERE id = ?
            """
            cursor.execute(comando_sql, (mensagem_id, ))
            mensagem_tupla = cursor.fetchone()

            if mensagem_tupla is None:
                return None
            
            mensagem = Mensagem(id=mensagem_tupla[0],usuario_from=mensagem_tupla[1],usuario_to=mensagem_tupla[2],mensagem=mensagem_tupla[3],chave_msg=mensagem_tupla[4])

            return mensagem
        except sqlite3.Error as error:
            print("Erro ao buscar id:", error)
        finally:
            if conexao:
                conexao.close()
    

    def criar_mensagem(self,mensagem):
    
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
            INSERT INTO mensagens (id, usuario_from, usuario_to, mensagem, chave_msg) 
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(comando_sql, \
                (mensagem.get_id(),mensagem.get_usuario_from(),mensagem.get_usuario_to(),mensagem.get_mensagem(),mensagem.get_chave_msg()))
            conexao.commit()
        except sqlite3.Error as error:
            print("Erro ao criar mensagem:", error)
        finally:
            if conexao:
                conexao.close()
        

    def deletar_mensagem(self, mensagem):
        conexao = None
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
                DELETE FROM mensagens WHERE id = ?
            """
            cursor.execute(comando_sql, (mensagem.get_id(), ))
            conexao.commit()
        except sqlite3.Error as error:
            print("Erro ao deletar mensagem:", error)
        finally:
            if conexao:
                conexao.close()

    def atualizar_chave(self, usuario_send, new_chave):
        try:
            conexao = sqlite3.Connection(self.db_path)
            cursor = conexao.cursor()
            comando_sql = """
            UPDATE mensagens SET chave_msg = ? WHERE email = ?
            """
            cursor.execute(comando_sql, (str(new_chave), usuario_send._email))
            conexao.commit()
        except sqlite3.Error as error:
            print("Erro ao atualizar mensagem:", error)
        finally:
            if conexao:
                conexao.close()
