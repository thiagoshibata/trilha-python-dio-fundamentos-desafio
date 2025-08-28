""" 
    Desafio:
        Criar as funções de sacar, depositar e extrato.
        Criar NOVAS funções: Criar usuário e criar conta corrente vinculada com o usuário.

    Passagem de argumentos:
        Saques (keyword only):
        Depósito (Positional only): 
        Extrato (Postional only e keyword only): saldo, argumentos nomeados: extrato

        Criar usuário
            - nome
            - dt_nascimento
            - cpf: somente numeros (string)
            - endereco: logradouro, num_casa, bairro, cidade/sigla estado.
            # Nao podemos cadastrar 2 usuários com o mesmo CPF
        Conta corrente:
            - armazenar em lista
            - agencia: 0001 (conta fixa)
            - conta: 1,2,3, etc.
            # Um usuário pode ter várias contas
        
        # filtre a lista de usuários buscando o número de CPF.
"""


menu = """

### BEM VINDO AO BANCO ###

Informe a operação que deseja efetuar:

[1] - Sacar
[2] - Depositar
[3] - Extrato
[4] - Sair

"""

saldo = 0
VALOR_LIMITE_MAX_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        if numero_saques < LIMITE_SAQUES_DIARIO:
            valor_saque = float(input("Digite o valor que deseja depositar: "))
            if valor_saque <= VALOR_LIMITE_MAX_SAQUE and valor_saque <= saldo and valor_saque != 0:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Débito: - R$ {valor_saque} \nSaldo: R$ {saldo}\n"
                print("Saque efetuado com sucesso!\n")
            else:
                print("\nO valor do saque é menor que o saldo atual ou excede o valor de 500,00\n")
        else:
            print("\n Limite de saque diário excedido! Tente novamente amanhã!")


    elif opcao == 2:
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito >= 0:
            saldo += valor_deposito
            extrato += f"Crédito: + R$ {valor_deposito} \nSaldo: R$ {saldo}\n"
            print("\nDepósito concluído com sucesso!\n")
        else:
            print("\n\n O valor informado não pode ser menor ou igual a R$ 0,00! Tente novamente!\n")

    elif opcao == 3:
        print("\n============ EXTRATO =============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    elif opcao == 4:
        break
    else:
        print("Operação inválida! Favor informar uma das opções do menu de operações!")
