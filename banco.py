import textwrap

def menu():
    menu = """
        =================SISTEMA BANCARIO =================

        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Criar Usuario
        0 - Sair

    -> """
    return input (textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
    else:
        print("Valor de deposito deve ser maior que 0")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Voce nao tem saldo suficiente!")
    elif excedeu_limite:
        print("Valor excede o limite!")
    elif excedeu_saques:
        print("Já ultrapassado o numero de saques permitidos")
    elif valor > 0:
        saldo -=valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print("Valor invalido!")
    
    return saldo, extrato

def exibir_extrato(saldo,/, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF somente numeros: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco": endereco})

    print("Usuario inserido com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF somente numeros: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario não encontrado!")




    

def main():
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0
        LIMITE_SAQUES = 3
        AGENCIA = "0001"
        usuarios = []
        contas = []

        while True:
            opcao = menu()

            if opcao == "1":
                valor = float(input("informe o valor:"))

                saldo, extrato = depositar(saldo, valor, extrato)
            
            elif opcao == "2":
                valor = float(input("informe o valor:"))

                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            
            elif opcao == "3":
                exibir_extrato(saldo, extrato=extrato)
            
            elif opcao == "4":
                criar_usuario(usuarios)
            
            elif opcao == "5":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)
            
            elif opcao == "0":
                print("Finalizando Aplicação....")
                break
            else:
                print("Digite uma opcao valida")
main()

        