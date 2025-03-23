import textwrap

def menu():
    menu = """
        =================SISTEMA BANCARIO =================

        1 - Depositar
        2 - Sacar
        3 - Extrato
        0 - Sair

    -> """
    return input (textwrap.dedent(menu))
def depositar(saldo, valor, extrato):
    valor = float(input("informe o valor:"))

    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
    else:
        print("Valor de deposito deve ser maior que 0")

    return saldo, extrato

def main():
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0
        LIMITE_SAQUES = 3

        while True:
            opcao = menu()

            if opcao == "1":
                saldo, extrato = depositar()
                #valor = float(input("informe o valor:"))

                #if valor > 0:
                    #saldo += valor
                    #extrato += f"Deposito: R$ {valor:.2f}\n"
                #else:
                    #print("Valor de deposito deve ser maior que 0")
            
            elif opcao == "2":
                valor = float(input("informe o valor:"))

                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES

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
                else:
                    print("Valor invalido!")
            
            elif opcao == "3":
                print("\n================ EXTRATO ================")
                print("Não foram realizadas movimentações." if not extrato else extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("==========================================")
            
            elif opcao == "0":
                print("Finalizando Aplicação....")
                break
            else:
                print("Digite uma opcao valida")
main()

        