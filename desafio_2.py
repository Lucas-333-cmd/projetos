import sys

saldoAtual = 0.0
saquesRealizados = 0
limiteSaques = 3
ultimoNumeroDeConta = 0
AGENCIA = '001'

clientes = {}


def gerarConta():
    global ultimoNumeroDeConta
    numeroConta = ultimoNumeroDeConta + 1
    if numeroConta > 9999:
        raise ValueError('NUMERO MAXIMO DE CONTAS ATIGINDO, CONTACTE O SUPORTE TÉCNICO')
    ultimoNumeroDeConta = numeroConta
    return str(numeroConta).zfill(4)


def inserirCPF():
    inserir = input('Qual seu CPF? (apenas números): ')
    cpf = ''.join(filter(str.isdigit, inserir))
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado


def inserirCliente():
    global clientes
    nome = input(str("Qual seu nome e sobrenome? "))
    nome = nome.upper()
    conta = gerarConta()
    cpfCliente = inserirCPF()
    idade = input(str("Quantos anos você tem? "))
    rua = input(str("Qual o nome da sua rua? "))
    bairro = input(str("Qual o seu bairro? "))
    bairro = bairro.capitalize()
    cidade = input(str("Qual a sua cidade? "))
    cidade = cidade.capitalize()
    estado = input(str("Qual o seu Estado? "))
    estado = estado.upper()
    endereco = f'{rua}, {bairro}, {cidade}-{estado}'
    clientes[nome] = {
        "cpf": cpfCliente,
        "conta": conta,
        "idade": idade,
        "endereco": endereco
    }
    print(f'''
    ==============BEM-VINDO!==============

                   Olá, {nome},
    seu número de conta 
    (e também seu user) é: {conta}. 
    sua agência é: {AGENCIA}
                LEMBRE-SE
    sua senha é seu CPF!!!


                #bancoREBOUÇAS
    =====================================
''')


def exibirClientes():
    clientesSalvos = clientes.copy()
    print(clientesSalvos)


def login():
    conta = input("Nome de usuário (conta): ")
    cpf = input("Senha (CPF): ")

    cpfFormatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    for nome, info_cliente in clientes.items():
        contaCliente = info_cliente.get("conta")
        cpfCliente = info_cliente.get("cpf")
        nomeCliente = info_cliente.get("nome")
        if contaCliente == conta and cpfCliente == cpfFormatado:
            print(f'''
                ====B=A=N=C=O==R=E=B=O=U=Ç=A=S====
                Bem vindo, {nomeCliente}

                            #bancoREBOUÇAS       
                ===================================]
                ''')

            return True
    print(f'''
     ====B=A=N=C=O=R==E=B=O=U=Ç=A=S====
        LOGIN OU SENHA ERRADO(S)

             #bancoREBOUÇAS       
    ===================================
    ''')
    return False


def deposito():
    global saldoAtual
    entrada = input("Quanto você deseja depositar? R$ ")
    entrada = entrada.replace(',', '.')

    try:
        valor_deposito = float(entrada)
        saldoAtual += valor_deposito
        print(f'''
        ================EXTRATO==============

        Depósito de: 
        R${entrada} 
        confirmado!


                      #bancoREBOUÇAS
        =====================================      

        ''')
    except ValueError:
        print('Valor Inválido')


def ver_saldo():
    global saldoAtual
    if saldoAtual == 0.0:
        print('Seu saldo ainda está zerado, deposite algo')
    else:
        print(f'''
        ================EXTRATO==============

        Seu saldo atual é de: 
        R$ {saldoAtual}


                    #bancoREBOUÇAS
        =====================================
''')


def saque():
    global saldoAtual, saquesRealizados
    limite_saque = 500
    if saquesRealizados >= 3:
        print('Limite de saques diários atingido.')
        return

    valorSaque = float(input('Quanto desejas sacar de vossa conta? R$ '))

    if valorSaque > limite_saque:
        print(f'''
        =!==!=!==!=!==!=EXTRATO=!==!=!==!=!==

                    VALOR DE SAQUE
                    EXCEDE O LIMITE
                          !!!


                    #bancoREBOUÇAS
        =====================================
    ''')
        return

    if valorSaque > saldoAtual:
        print(f'''
        =!==!=!==!=!==!=EXTRATO=!==!=!==!=!==
                    SALDO INSUFICIENTE

            Seu saldo atual é de: 
            R${saldoAtual}


                    #bancoREBOUÇAS            
        ====================================                                      
            ''')
        return

    saldoAtual -= valorSaque
    saquesRealizados += 1
    print(f'''
    ================EXTRATO==============

        Seu saque de: 
        R$ {valorSaque} 
        foi realizado com sucesso,


        Seu novo saldo é de: 
        R$ {saldoAtual}


                #bancoREBOUÇAS       
    ====================================
    ''')


def main():
    telaInicial = '''
                                     #BANCO REBOUÇAS#

                        (1)Depósito                     (2)Saldo

                        (3)Saque                        (4)Novo Cliente

                        (5)Lista de Clientes            (6)Acessar Conta

                        (7)Sair

    '''

    login_bem_sucedido = False

    while True:
        user = int(input(f'{telaInicial}Qual operação deseja realizar?: '))

        if user == 4:
            inserirCliente()
        elif user == 7:
            print('Obrigado por utilizar o Banco Rebouças. Volte Sempre!')
            break
        elif user == 6:
            loginResultado = login()
            if loginResultado:
                login_bem_sucedido = True
        if not login_bem_sucedido:
            print('''
            ====B=A=N=C=O==R=E=B=O=U=Ç=A=S====

            Você precisa ACESSAR CONTA se quiser
                    realizar alguma operação.


                    #bancoREBOUÇAS  
            ''')
            continue

        if user == 1:
            deposito()
        elif user == 2:
            ver_saldo()
        elif user == 3:
            saque()
        elif user == 5:
            exibirClientes()
        else:
            print('Opção Inválida. Escolha um número entre 1 e 7')

    if saldoAtual == 0.0:
        print('''

        ====B=A=N=C=O==R=E=B=O=U=Ç=A=S====

        (1) Acessar Conta                 
        (2) Sair

        ''')

    user = int(input(f'{telaInicial}Qual operação deseja realizar?: '))

    if user == 1:
        login()
    elif user == 2:
        print('Obrigado por utilizar o Banco Rebouças. Volte Sempre!')
        sys.exit()

    else:
        print("Opção Inválida")


main()