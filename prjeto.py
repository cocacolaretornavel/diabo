
todos_conjuntos = []
opcao = ' '
sair = 'nao'




def menu_geral():
    print("[0] - Sair")
    print("[1] - Criar conjunto")
    print("[2] - Adicionar elemento a um conjunto")
    print("[3] - Remover elemento de um conjunto")
    print("[4] - Mostrar conjuntos")
    print("[5] - Apagar conjuntos")
    print("[6] - Unir conjuntos")
    print("[7] - Checar conjunto")




    global opcao
    opcao = int(input("Digite a opção: "))
   
    return opcao


def criar_conjunto():
    conj = []
    nome = input('Insira o nome do conjunto: ')
    conj.append(nome)
    ni = int(input('Insira a quantidade de elementos do conjunto: '))
   
   
    for x in range(ni):
        item = int(input('Qual numero a ser adicionado? '))
        while item in conj:
            print('O número já está no conjunto. Números duplicados não são permitidos.')
            item = int(input('Qual número a ser adicionado? '))
        conj.append(item)
    
    global todos_conjuntos
    todos_conjuntos.append(conj)
    print(todos_conjuntos)


def add_elemento():

    pesquisa = input('Selecione o conjunto a ser manipulado: ')
    print(len(todos_conjuntos))

    for i in range(len(todos_conjuntos)):

        if todos_conjuntos[i][0] == pesquisa:
            item = int(input('insira o número a ser adicionado: '))
            while item in todos_conjuntos[i]:
                print('O número já está no conjunto. Números duplicados não são permitidos.')
                item = int(input('insira o número a ser adicionado: '))
            todos_conjuntos[i].append(item)
        else:
            pass

def remove_elemento():

    pesquisa = input('Selecione o conjunto a ser manipulado: ')
    print(len(todos_conjuntos))

    for i in range(len(todos_conjuntos)):

        if todos_conjuntos[i][0] == pesquisa:
            item = int(input('insira o número a ser removido: '))
            while item not in todos_conjuntos[i]: 
                print('O número não existe nesse conjunto, insira um número existente')
                item = int(input('insira o número a ser removido: '))
            todos_conjuntos[i].remove(item)
            
        else:
            pass

def mostrar():
    print(20*'-')
    print('TODOS OS CONJUNTOS CRIADOS')

    if len(todos_conjuntos) == 0:
        print('VAZIO')
        print(' ')
    else:
        for item in range(len(todos_conjuntos)):
            print(todos_conjuntos[item])
    print(20*'-')      
            
def delete():
    pesquisa = input('insira o nome do conjunto a ser deletado: ')

    for i in range(len(todos_conjuntos)):
        if todos_conjuntos[i][0]  == pesquisa:
            todos_conjuntos.pop(i)
        else:
            pass
   
while sair == 'nao':
    menu_geral()
    if opcao == 0:
        sair = 'sim'
    elif opcao == 1:
        criar_conjunto()
    elif opcao == 2:
        add_elemento()
    elif opcao == 3:
        remove_elemento()
    elif opcao == 4:
        mostrar()
    elif opcao == 5:
        delete()


else:
    print('Programa finalizado.')

