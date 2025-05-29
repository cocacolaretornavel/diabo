todos_conjuntos = [] #estabelecendo a lista em que todos os conjuntos do usuário serão armazenados
nomes = [] # nome dos conjuntos, serve para evitar conjuntos com o mesmo nome durante a criação de novos conjuntos.
opcao = ' ' # variável que o valor vai definir qual ação será realizada
sair = 'nao' # variável que serve posteriormente para definir se o programa vai continuar rodando ou se vai ser finalizado.




def menu_geral():
    print("[0] - Sair")
    print("[1] - Criar conjunto")
    print("[2] - Adicionar elemento a um conjunto")
    print("[3] - Remover elemento de um conjunto")
    print("[4] - Mostrar conjuntos")
    print("[5] - Apagar conjuntos")
    print("[6] - Unir conjuntos")
    print("[7] - Checar interseção de conjuntos")




    global opcao #tornando a variável global para que a mudança do valor seja reconhecida por fora da função
    opcao = int(input("Digite a opção: "))
   
    return opcao

def criar_conjunto():
    conj = [] #lista onde os elementos e o nome do conjunto criado pelo usuário vão ser guardados
    global nomes
    nome = input('Insira o nome do conjunto: ')
    while nome in nomes:
        nome = input('Um conjunto já possui esse nome, escolha outro: ')
    conj.append(nome)
    nomes.append(nome)

    #while nome in nomes verifica se já existe um conjunto registrado com o nome escolhido com o usuário. serve para evitar erros durante as ações que requerem saber
    #os nomes do conjuntos.

    ni = int(input('Insira a quantidade de elementos do conjunto: ')) #ni = numero de itens. serve para o loop for em seguida, definindo a quantidade de repetições.
   
   
    for x in range(ni):
        item = int(input('Qual numero a ser adicionado? '))
        while item in conj:
            print('O número já está no conjunto. Números duplicados não são permitidos.')
            item = int(input('Qual número a ser adicionado? '))
        conj.append(item)
    
    #o loop vai utilizar a variável item para guardar cada elemento inserido pelo usuário. o while intem in conj serve para checar se o número já está no conjunto.
    #se estiver ele não adiciona e pergunta novamente até que o usuário insira um número válido.
    global todos_conjuntos #tornando todos_conjuntos global para que as mudanças feitas nela possam ser acessadas pelo restante do programa
    todos_conjuntos.append(conj)
    print(f'O conjunto {conj[0]} foi adicionado com sucesso!')

def add_elemento():

    pesquisa = input('Selecione o conjunto a ser manipulado: ') #variavel pesquisa serve para registrar o nome do conjunto para depois o loop identificar
    #qual conj tem esse nome (elemento 0).
    
    for i in range(len(todos_conjuntos)):

        if todos_conjuntos[i][0] == pesquisa:
            item = int(input('insira o número a ser adicionado: '))
            while item in todos_conjuntos[i]:
                print('O número já está no conjunto. Números duplicados não são permitidos.')
                item = int(input('insira o número a ser adicionado: '))
            todos_conjuntos[i].append(item)
        else:
            pass
    # o loop primeiro vai estabelecer quantos conjuntos vão ter que ser verificados, em seguida verifica-se se o primeiro item da lista (nome) é equivalente
    # ao nome procurado pelo usuário. Depois disso o while item in todos os conjuntos[i] vai checar se já existe um elemento com o valor que será inserido no conjunto
    # nomeado como a pesquisa. Se sim, o loop continua perguntando até que um valor não existente na lista seja escolhido.
    print(f'O elemento {item} foi adicionado ao conjunto {pesquisa}.')

def remove_elemento():

    pesquisa = input('Selecione o conjunto a ser manipulado: ')


    for i in range(len(todos_conjuntos)):

        if todos_conjuntos[i][0] == pesquisa:
            item = int(input('insira o número a ser removido: '))
            while item not in todos_conjuntos[i]: 
                print('O número não existe nesse conjunto, insira um número existente')
                item = int(input('insira o número a ser removido: '))
            todos_conjuntos[i].remove(item)
            
        else:
            pass
    
    print(f'O elemento {item} foi removido do conjunto {pesquisa}.')
    #funciona do mesmo modo que a função add_elemento(), com a diferença de que o item é removido.

def mostrar():
    print(20*'-')
    print('TODOS OS CONJUNTOS CRIADOS')

    # os dois prints servem para deixar a interface mais decorada

    if len(todos_conjuntos) == 0: # esse if tem o propósito de verificar se existe algum conjunto armazenado na lista todos_conjuntos.
        print('NENHUM CONJUNTO CRIADO')
        print(' ')
    else:
        print('Os conjuntos criados são:')
        for item in range(len(todos_conjuntos)):
            print(todos_conjuntos[item])

    # caso existam conjuntos armazenados em todos_conjuntos, item vai contar quantos conjuntos tem na lista e printar cada um deles

    print(20*'-')  # decoração de novo    
            
def delete():
    pesquisa = input('insira o nome do conjunto a ser deletado: ')

    for i in range(len(todos_conjuntos)):
        if todos_conjuntos[i][0]  == pesquisa:
            todos_conjuntos.pop(i)
        else:
            pass
    print(f'O conjunto {pesquisa} foi deletado com sucesso.')

    #a função procura por um conjunto que tenha o item de índice 0 (nome) igual ao pesquisado pelo usuário do programa e o remove da lista todos_conjuntos
   
def unir():
    
    print('Escolha dois conjuntos para unir')
    pesquisa = [] # pesquisa é a lista onde os dois nomes dos conjuntos serão guardados para depois serem usados
    unidos = [] # armazena os elementos de ambos os conjuntos

    for x in range(2):
        conjunto = input(f'Conjunto {x+1}: ')
        pesquisa.append(conjunto)
    # esse loop tem o propósito de perguntar ao usuário quais conjuntos ele quer unir.
    # for x in range(2) define que a pergunta será feita duas vezes, já que é a quantidade do conjuntos permitida unir.
    # pesquisa.append(conjunto) adiciona à lista pesquisa os valores armazenados na variável conjunto.
    
    for i in range(len(todos_conjuntos)):
        if todos_conjuntos[i][0] == pesquisa[0]:
            for item in todos_conjuntos[i]:
                if not item == todos_conjuntos[i][0]:
                    unidos.append(item)
                else:
                    pass
            break
        else:
            pass
    # O loop vai se repetir a quantidade de itens em todos_conjuntos procurando um conj que tenha o índice zero igual ao primeiro item
    # da lista pesquisa. Depois, cada item no conjunto encontrado vai ser colocado na lista unidos (com a excessão do item de índice zero, porque
    # esse é o nome (if not item == todos_conjuntos[i][0] checa isso antes de adicionar o item))

    for b in range(len(todos_conjuntos)):
        if todos_conjuntos[b][0] == pesquisa[1]:
            for item in todos_conjuntos[b]:
                if not item == todos_conjuntos[b][0]:
                    if not item in unidos:
                        unidos.append(item)
                else:
                    pass
            break
        else:
            pass
    # esse loop funciona do mesmo jeito que o anterior, mas ele busca um conj que tenha o índice 0 equivalente ao segundo item da lista pesquisa. if not item in unidos
    # é acrescentado ao código para checar se existem números repetidos nos conjuntos, garantindo que não apareçam números duplicados na união de conjuntos.
     
    print(f'A união dos conjuntos {pesquisa[0]} e {pesquisa[1]} é {unidos}.')

def intersec():

    elementos = [] # elementos armazena os elementos de ambos os conjuntos que serão escolhidos pelo usuário
    intersecao = [] # intersecao armazena os elementos que se encontram nos dois conjuntos simultaneamente

    print('Escolha dois conjuntos para checar a interseção: ')
    pesquisa = []

    for x in range(2):
        conjunto = input(f'Conjunto {x+1}: ')
        pesquisa.append(conjunto)
    
    # o loop funciona do mesmo modo que na função unir()
    
    for i in range(len(todos_conjuntos)):
        if todos_conjuntos[i][0] == pesquisa[0]:
            for item in todos_conjuntos[i]:
                if not item == todos_conjuntos[i][0]:
                    elementos.append(item)
                else:
                    pass
            break
        else:
            pass

    # usando a mesma lógica da pesquisa em unir(), o loop adiciona todos os item do primeiro conjunto escolhido a lista elementos, com a excessão do item de índice
    # 0, porque ele é o nome do conjunto.

    for b in range(len(todos_conjuntos)):
        if todos_conjuntos[b][0] == pesquisa[1]:
            for item in todos_conjuntos[b]:
                if not item == todos_conjuntos[b][0]:
                    if item in elementos:
                        intersecao.append(item)
                else:
                    pass
            break
        else:
            pass

    # esse loop verifica qual conj possui o item 0 com o mesmo nome do item 1 da lista pesquisa. Depois de desconsiderar o nome do conjunto (item de índice 0), if
    # item in elementos checa se cada item desse conjunto está na lista elementos. Os que estiverem, são adicionados à lista intersecao.

    print(f'a interseção dos conjuntos é {intersecao}')
    if len(intersecao) == 0:
        print('Não existe interseção entre esses conjuntos!')
    # essa parte do código serve mais para melhorar a interação com o usuário. if len(intersecao) == 0 vê se a lista é vazia, ou seja se a interseção dos conjuntos
    # é inexistente e diz isso para o usuário.



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
    elif opcao == 6:
        unir()
    elif opcao == 7:
        intersec()
    else:
        print('Opcão inválida! Escolha outra.')

# while sair == 'nao' verifica se o programa deve ser encerrado ou não. Caso não seja encerrado, cada if e elif verifica qual valor a variável opcao recebeu em 
# menu_geral() e, de acordo com isso, chama uma função em específico. Caso a opcão escolhida não exista, o programa avisa para o usuário e chama de novo a função 
# menu_geral().

# Quando o programa sair do loop, ou seja, quando 0 for escolhido e sair ter seu valor alterado para 'sim', o código acaba.

print('Programa finalizado.')

