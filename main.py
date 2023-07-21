import sys

telaInicial = '''
                                 #BANCO REBOUÇAS#
                    
                    (1)Depósito                     (2)Saldo
        
                    (3)Saque                        (4)Sair
                                    
'''

saldoAtual = 0.0
saquesRealizados = 0

limiteSaques = 3


def deposito():
    global saldoAtual
    entrada = input("Quanto você deseja depositar? R$ ")
    entrada = entrada.replace(',', '.')

    try:
        valor_deposito = float(entrada)
        saldoAtual += valor_deposito
        print(f'Depósito de R${entrada} confirmado.')
    except ValueError:
        print('Valor Inválido')


def ver_saldo():
    global saldoAtual
    if saldoAtual == 0.0:
        print('Seu saldo ainda está zerado, deposite algo')
    else:
        print(f'Seu saldo atual é de: R$ {saldoAtual}')


def saque():
    global saldoAtual, saquesRealizados
    limite_saque = 500
    if saquesRealizados >= 3:
        print('Limite de saques diários atingido.')
        return

    valorSaque = float(input('Quanto desejas sacar de vossa conta? R$ '))

    if valorSaque > limite_saque:
        print(f'''

                                                VALOR DE SAQUE
                                                EXCEDE O LIMITE
                                                      !!!
    ''')
        return

    if valorSaque > saldoAtual:
        print(f'''
                                               SALDO INSUFICIENTE
                                           Seu saldo atual é de R${saldoAtual}
                                                  
            ''')
        return

    saldoAtual -= valorSaque
    saquesRealizados += 1
    print(f'''
                                    #Seu saque de R$ {valorSaque} foi realizado com sucesso,
                                        #Seu novo saldo é de: R$ {saldoAtual}
        
    ''')


while True:
    user = int(input(f'{telaInicial}Qual operação deseja realizar?: '))

    if user == 1:
        deposito()
    elif user == 2:
        ver_saldo()
    elif user == 3:
        saque()
    elif user == 4:
        print('Obrigado por utilizar o Banco Rebouças. Volte Sempre!')
        break
else:
    print('Opção Inválida. Escolha um número entre 1 e 4')

if saldoAtual == 0.0:
    print('''
                        Seu saldo continua ZERADO!
                        Por favor, deposite algo.
                        
                                 #BANCO REBOUÇAS#
                                    
                    (1) Depósito                    (2) Sair
                        
    ''')

user = int(input(f'{telaInicial}Qual operação deseja realizar?: '))


if user == 1:
    deposito()
elif user == 2:
    print('Obrigado por utilizar o Banco Rebouças. Volte Sempre!')
    sys.exit()

else:
    print("Opção Inválida")
