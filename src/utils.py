import sqlite3
import string
from random import choice
import urllib, urllib.request
import smtplib
import email.message
import app


#funções que não envolvem diretamente o banco de dados

def criar_banco_de_dados(db_path):   

    conexao = sqlite3.connect(db_path)

    comando_sql_usuario = """
    CREATE TABLE usuarios (
        cpf TEXT NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        contatos TEXT,
        chave_user TEXT NOT NULL
    )
    """

    #adicionar lógica de operação por chave unica de mensagem
    #gerar chaves distintas
    comando_sql_mensagem = """ 
    CREATE TABLE mensagens (
        id TEXT NOT NULL,
        usuario_from TEXT NOT NULL,
        usuario_to TEXT NOT NULL,
        mensagem TEXT NOT NULL,
        chave_msg TEXT NOT NULL
    )
    """


    cursor = conexao.cursor()

    cursor.execute(comando_sql_usuario)

    cursor.execute(comando_sql_mensagem)

    conexao.close()

    print('\n\n  Banco de Dados Criado com Sucesso!')

def gerar_nova_senha():
    tamanho = 12
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)

    return (senha)    

def mandar_email(email_from:str,email_to:str,senha_app:str,nova_senha:str,assunto:str,usuario_existente):
    corpo_email = f"""
    <p>  Oi {usuario_existente._nome}, sua nova senha é {nova_senha}.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = email_from #email padrão
    msg['To'] = email_to
    password = str(senha_app) 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('\n\n  Email enviado')

    usuario_existente.set_senha(nova_senha)
    
    conexao = sqlite3.connect(app.usuario_dao.db_path)

    cursor = conexao.cursor()

    comando_sql = """
        UPDATE usuarios SET senha = ? WHERE cpf = ?
    """
    
    cursor.execute(comando_sql, (nova_senha,usuario_existente._cpf))

    conexao.commit()
    conexao.close()

def encaminhar_email(email_from:str,email_to:str,senha_app:str,assunto:str,mensagem:str,usuario_send,usuario_existente,mensagem_id):
    corpo_email = f"""
    <p>  Oi {usuario_send._nome}, você tem uma nova mensagem segura de {usuario_existente._nome}.</p>
    <p> <br> <br> {mensagem} com o código: {mensagem_id} </p>
    """

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = email_from #email padrão
    msg['To'] = email_to
    password = str(senha_app) 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('\n\n  Email enviado')

def gerar_chave():
    tamanho = 12
    valores = string.ascii_lowercase + string.digits
    chave_user = ''
    for i in range(tamanho):
        chave_user += choice(valores)

    return (chave_user) 

def gerar_id():
    tamanho = 25
    valores = string.ascii_lowercase + string.digits
    id_val = ''
    for i in range(tamanho):
        id_val += choice(valores)

    return (id_val)