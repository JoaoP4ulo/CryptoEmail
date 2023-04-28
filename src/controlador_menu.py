from src.classes_base import Usuario
import src.controlador_sistema as sistema
import smtplib
import email.message
import src.utils as utils
import sqlite3
import app
import src.funcao as funcao

#funções chamadas pelo menu principal


def menu_principal():
    while True:

        print('\n\n\n --------- Menu Principal --------- \n')

        print('  1 – Fazer login')
        print('  2 – Recuperar Senha')
        print('  3 – Cadastrar Novo Usuario')
        print('  4 – Sair')
    

        opcao = input('\n  Digite a opção desejada: ')

        if opcao == '1':
            menu_fazer_login(app.usuario_dao)
        elif opcao == '2':
            menu_recuperar_senha(app.usuario_dao,app.senha)
        elif opcao == '3':
            menu_cadastrar_usuario(app.usuario_dao)
        elif opcao == '4':
            print('\n\n  Saindo do sistema ...')
            break
        else:
            print('\n\n  Opção Inválida!')



def menu_cadastrar_usuario(usuario_dao):

    cpf = (input('\n\n  CPF: '))
    while len(cpf) != 11:
        print('\n\n  CPF fora do padrão (xxxyyyzzzww), tente novamente. ')
        cpf = (input('\n  CPF: '))
        if len(cpf) != 11:
            menu_principal()
    usuario_existente = usuario_dao.buscar_usuario(cpf)
       

    if usuario_existente is not None:
        print('\n    CPF já cadastrado!')
        cpf = input('\n  Digite um novo CPF: ')
        usuario_existente = usuario_dao.buscar_usuario(cpf)
        if usuario_existente is not None:
            print('\n    CPF já cadastrado. Erro no cadastro!')
            menu_principal()

    nome = input('  Nome: ')

   
    email = input('  Email: ')

    senha = input('  Senha: ')

    senha_confirm= input('  Confirmar senha: ')
    while senha_confirm != senha:
        print(' Senhas incompativeis. Tente novamente!')
        senha_confirm= input('  Confirmar senha: ')

    chave = funcao.criar_chave()
    chave_user = utils.gerar_chave()

    usuario = Usuario(cpf, nome, email, senha, chave, contatos="[]", chave_user=chave_user)

    usuario_dao.cadastrar_usuario(usuario)

    print('\n\n  Usuario cadastrado com sucesso!')




def menu_fazer_login(usuario_dao):

    
    cpf = input('\n\n  CPF: ')

    usuario_existente = usuario_dao.buscar_usuario(cpf)

    if usuario_existente is None:
        print('\n    CPF invalido!')
        cpf = input('\n  Digite um novo CPF: ')
        usuario_existente = usuario_dao.buscar_usuario(cpf)
        if usuario_existente is None:
            menu_principal()
   
    
    senha = input('\n\n  Senha: ')
    if senha != usuario_existente._senha:
        print('\n  Senha incorreta. Tente Novamente!')
        senha = input('\n\n  Senha: ')
        if senha != usuario_existente._senha:
            print('\n  Senha incorreta. Erro no cadastro!')
            menu_principal()

    #menu secundário

    sistema.menu_sistema(usuario_existente)



def menu_recuperar_senha(usuario_dao,senha_app):

    e_mail = input('\n\n  Email: ')

    usuario_existente = usuario_dao.buscar_email(e_mail)

    while usuario_existente is None:
        print('\n    Email invalido!')
        cpf = input('\n  Digite um novo Email: ')
        usuario_existente = usuario_dao.buscar_email(e_mail)
    
    nova_senha = utils.gerar_nova_senha()

    utils.mandar_email(app.email_from,e_mail,app.senha,nova_senha,'Recuperacao de Senha',usuario_existente)


