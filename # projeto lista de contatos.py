#projeto lista de contatos
#LETÍCIA E BEATRIZ
opcao = 'nulo'
sair = 'nao'
agenda = {}

import json




def menu_geral():
    print("[0] - Sair")
    print("[1] - Adicionar contato")
    print("[2] - Buscar contato")
    print("[3] - Editar contato")
    print("[4] - Remover contato")
    print("[5] - Salvar//carregar agenda")
    print("[6] Visualizar lista")

    global opcao
    opcao = input("Digite a opção: ")
    opcao = int(opcao)

    return opcao


def add_contato(usuario: str, nome: str, telefone: str, email: str, agenda: dict =  "agenda"):

    while usuario[0] != '@':
        print("Erro! Você precisa inserir o '@'.")
        usuario = input("Insira o nome do usuário: ")
    while usuario in agenda:
        usuario = input("User já é utilizado, escolha outro: ")

    while len(telefone) != 11 and "-" not in telefone:
        print("Esse número é inválido. Use os 11 digitos e o '-'.")
        telefone = input("Insira o número de telefone: ")

    while "@" not in email or "." not in email:
        print("Este e-mail inválido. Está faltando '@' ou/e '.'")
        email = input("Insira o e-mail: ")

    agenda[usuario] = [nome, telefone, email]
    print(f'O contato {usuario} foi adicionado.')


def buscar_contato (usuario: str, agenda: dict =  "agenda"):

    while usuario not in agenda:
        print('Esse usuário não está cadastrado, tente outro.')
        usuario = input(f'Insira o user do usuário desejado: ')

    else:
        print(f'Os dados de {usuario} são {agenda[usuario]}')


def edit_cont(usuario: str, campo: str, novo_valor: str, agenda: dict =  "agenda"):

    while usuario not in agenda:
        usuario = input('Esse usuário não está na agenda! Insira um que esteja: ')

    while not campo == 'nome' and not campo == 'telefone' and not campo == 'email':
        campo = input("CAMPO INVALIDO. Insira um campo [nome, telefone, email]: ")

    if campo == 'nome':
        agenda[usuario][0] = novo_valor
    elif campo == 'telefone':
        while len(novo_valor) != 11 or '-' not in novo_valor:
            novo_valor = input('O telefone precisa ter "-" e 11 dígitos. Tente novamente: ')
        agenda[usuario][1] = novo_valor
    elif campo == 'email':
        while '@' not in novo_valor and '.' not in novo_valor:
            novo_valor = input('O email precisa ter "@" e pelo menos um ".", tente novamente: ')
        agenda[usuario][2] = novo_valor


    print(f'Os dados de {usuario} foram alterados. Dados atuais:')
    print(f'Nome completo: {agenda[usuario][0]}\n Telefone: {agenda[usuario][1]}\n Email: {agenda[usuario][2]}')


def remove(usuario: str, agenda: dict =  "agenda"):

    if len(agenda) == 0:
        print('A agenda está vazia.')
    else:
        while usuario not in agenda:
            usuario = input('Esse usuário não está na agenda! Escolha outro: ')
        del agenda[usuario]
        print(f'O usuário {usuario} foi removido da agenda')


def salvar():
    global agenda

    with open("agenda.json","r+") as arquivojason:
        json.dump(agenda, arquivojason)


def carregar():
    global agenda

    with open("padrao.json", "r+") as agendajson:
        agenda = {}
        agenda = json.load(agendajson)
    print(agenda)

def ver():
    global agenda

    if len(agenda) != 0:
        for k in agenda.keys():
            print(f'Usuário: {k}\n Nome completo: {agenda[k][0]}\n Telefone: {agenda[k][1]}\n Email: {agenda[k][2]}\n')
    else:
        print('A agenda está vazia')



while sair == 'nao':
    menu_geral()
    usuario = ' '
    if opcao == 1:
        usuario = input('Insira o user do usuario: ')
        nome = input('Insira o nome completo do usuário: ')
        telefone = input('Insira o telefone do usuário: ')
        email = input('Insira o email do usuário: ')

        add_contato(usuario, nome, telefone, email, agenda)
    elif opcao == 2:
        usuario = input('Insira o user que você deseja verificar: ')

        buscar_contato(usuario, agenda)
    elif opcao == 3:
        print('Os campos são: nome, telefone, e email')

        usuario = input('Digite o user do usuário a ser editado: ')
        campo = input('Insira o campo a ser modificado: ')
        novo_valor = input('Insira o novo valor do campo: ')

        edit_cont(usuario, campo, novo_valor, agenda)

    elif opcao == 4:
        usuario = input('Insira o user que deseja remover: ')

        remove(usuario, agenda)
    elif opcao == 5:
        salvar_ou_carregar = input('Qual operação você deseja realizar? "s" para salvar, "c" para carregar arquivo: ')
        if salvar_ou_carregar == 'S' or salvar_ou_carregar == 's':
            salvar()
        elif salvar_ou_carregar == 'c' or salvar_ou_carregar == 'C':
            carregar()
    elif opcao == 6:
        ver()

    elif opcao == 0:
        sair = 'sim'

    else:
        print('Opção inválida, insira outra.')

print('PROGRAMA FINALIZADO;')