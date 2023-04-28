import sqlite3
from src.classes_dao import UsuarioDAO
from src.classes_base import Usuario
import app
import email.message
import smtplib
import src.funcao as funcao
import numpy as np
import string
import src.utils as utils
import src.controlador_menu as menu


#funções chamdas pelo menu de usuario


def menu_sistema(usuario_existente):
    while True:

        print('\n\n\n --------- Sistema de Cadastro --------- \n')

        print('  1 – Realizar Busca Arxiv')
        print('  2 – Adicionar Contato')
        print('  3 – Listar Contatos')
        print('  4 – Atualizar Dados')
        print('  5 – Voltar Menu Principal')
    

        opcao = input('\n  Digite a opção desejada: ')

        if opcao == '1':
            enviar_email(app.usuario_dao,usuario_existente)
        elif opcao == '2':
            adicionar_contato(app.usuario_dao,usuario_existente)
        elif opcao == '3':
            listar_contatos(app.usuario_dao,usuario_existente)
        elif opcao == '4':
            atualizar_dados(app.usuario_dao,usuario_existente)
        elif opcao == '5':
            print('\n\n  Saindo do sistema ...')
            menu.menu_principal()
        else:
            print('\n\n  Opção Inválida!')


def adicionar_contato(usuario_dao,usuario_existente):

    
    email = input('\n\n  Email: ')

    usuario_send = usuario_dao.buscar_email(email)

    if usuario_send is None:
        print('\n    Email invalido!')
        email = input('\n  Digite um novo email: ')
        usuario_send = usuario_dao.buscar_email(email)
        if usuario_send is None:
            menu_sistema(usuario_existente)
    
    usuario_dao.adicionar_contato(usuario_existente,usuario_send)

    


def enviar_email(usuario_dao,usuario_existente):

    remetente_lista = []

    qtd_remetentes = int(input("\n Quantos remetentes: "))
    for n in range(qtd_remetentes):

        remetente = input('\n\n  Remetente: ')
        usuario_send = usuario_dao.buscar_email(remetente)

        if usuario_send is None:
            print('\n    Email invalido!')
            remetente = input('\n  Digite um novo email: ')
            usuario_send = usuario_dao.buscar_email(remetente)
            if usuario_send is None:
                menu_sistema(usuario_existente)
        remetente_lista.append(remetente)


    assunto = str(input("\n Assunto: "))
    frase = str(input('\n  Digite a mensagem: '))

    codigo = []
    codigo_inv = []
    identidade = [[1,0],[0,1]]

    chave = eval(usuario_existente.get_iduser())
    chave_inv = np.linalg.inv(chave)

    lista = funcao.letra_em_numero(frase)
    matriz = funcao.transformar_matriz(lista)
    for i in range(len(matriz)):
        matriz_chave=funcao.codifiar(chave,matriz[i])
        codigo.append(matriz_chave)

    for j in range(len(matriz)):
        matriz_chave=funcao.codifiar(chave_inv,codigo[j])
        codigo_inv.append(matriz_chave)

    lista_contatos = eval(usuario_existente.get_contatos())

    for i in range(len(remetente_lista)):
        usuario_send = usuario_dao.buscar_email(remetente_lista[i])

        if remetente_lista[i] in lista_contatos:
            utils.encaminhar_email(app.email_from,usuario_send.get_email(),app.senha,assunto,frase,usuario_send,usuario_existente)
        else:
            utils.encaminhar_email(app.email_from,usuario_send.get_email(),app.senha,assunto,codigo,usuario_send,usuario_existente)

    print("\n\n   Email enviado!")




def listar_contatos(usuario_dao,usuario_existente):
    contatos = usuario_existente.get_contatos()
    lista_contatos = eval(contatos)
    print(lista_contatos)



def atualizar_dados(usuario_dao,usuario):

    conexao = sqlite3.connect(usuario_dao.db_path)

    cursor = conexao.cursor()


    op_nome=input('\n Deseja alterar o nome (y/n): ')
    if op_nome=='y':
        nome=input("\n Nome: ")
        usuario.set_nome(nome)

        comando_sql_nome = """
        UPDATE usuarios SET nome = ? WHERE cpf = ?
        """
        cursor.execute(comando_sql_nome, (nome,usuario._cpf))
        conexao.commit()

    op_email=input('\n Deseja alterar o email (y/n): ')
    if op_email=='y':
        email=input("\n Email: ")
        usuario.set_email(email)

        comando_sql_email = """
        UPDATE usuarios SET email = ? WHERE cpf = ?
        """
        cursor.execute(comando_sql_email, (email,usuario._cpf))
        conexao.commit()

    op_senha=input('\n Deseja alterar a senha (y/n): ')
    if op_senha=="y":
        senha=input("\n Senha: ")
        usuario.set_senha(senha)

        comando_sql_senha = """
        UPDATE usuarios SET senha = ? WHERE cpf = ?
        """
        cursor.execute(comando_sql_senha, (senha,usuario._cpf))
        conexao.commit()

    conexao.close()
    
