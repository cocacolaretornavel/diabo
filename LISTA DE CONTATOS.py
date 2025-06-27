# projeto lista de contatos
opcao = ' '
sair = 'nao'
agenda = {}


def menu_geral():
    print("[0] - Sair")
    print("[1] - Adicionar contato")
    print("[2] - Buscar contato")
    print("[3] - Editar contato")
    print("[4] - Remover contato")
    print("[5] - Salvar agenda")
    print("[6] - Carregar agenda")

    global opcao
    opcao = int(input("Digite a opção: "))

    return opcao


def add_contato(agenda: "agenda", usuario: str, nome: str, telefone: str, email: str):
    while usuario[0] != '@':
        print("Erro! Você precisa inserir o '@'.")
        usuario = input("Insira o nome do usuário: ")

    while len(telefone) != 11 and "-" not in telefone:
        print("Esse número é inválido. Use os 11 digitos e o '-'.")
        telefone = input("Insira o número de telefone: ")

    while "@" not in email or "." not in email:
        print("Este e-mail inválido. Está faltando '@' ou/e '.'")
        email = input("Insira o e-mail: ")

    agenda[usuario] = [nome, telefone, email]
    print(f'O contato {usuario} foi adicionado.')


def buscar_contato(agenda: "agenda", usuario: str):

    while usuario not in agenda:
        print('Esse usuário não está cadastrado, tente outro.')
        usuario = input(f'Insira o user do usuário desejado: ')

    else:
        print(f'Os dados de {usuario} são {agenda[usuario]}')


def edit_cont(agenda: "agenda", usuario: str, campo: str, novo_valor: str):

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


def remove(agenda: "agenda", usuario: str):

    if len(agenda) == 0:
        print('A agenda está vazia.')
    else:
        while usuario not in agenda:
            usuario = input('Esse usuário não está na agenda! Escolha outro: ')
        del agenda[usuario]
        print(f'O usuário {usuario} foi removido da agenda')

def salvar(agenda: "agenda"):

    import json
    agenda.json = json.dumps(agenda)




while sair == 'nao':
    menu_geral()
    usuario = ' '
    if opcao == 1:
        usuario = input('Insira o user do usuario: ')
        nome = input('Insira o nome completo do usuário: ')
        telefone = input('Insira o telefone do usuário: ')
        email = input('Insira o email do usuário: ')

        add_contato(agenda, usuario, nome, telefone, email)
    elif opcao == 2:
        usuario = input('Insira o user que você deseja verificar: ')

        buscar_contato(agenda, usuario)
    elif opcao == 3:
        print('Os campos são: nome, telefone, e email')

        usuario = input('Digite o user do usuário a ser editado: ')
        campo = input('Insira o campo a ser modificado: ')
        novo_valor = input('Insira o novo valor do campo: ')

        edit_cont(agenda, usuario, campo, novo_valor)

    elif opcao == 4:
        usuario = input('Insira o user que deseja remover: ')

        remove(agenda, usuario)

    elif opcao == 0:
        sair = 'sim'

    else:
        print('Opção inválida, insira outra.')

print('PROGRAMA FINALIZADO;')