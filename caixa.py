saldo = 0
extrato = []

def first_deposito():
    global saldo
    global extrato
    if saldo == 0:
        primeiro_deposito = input("Seja bem-vindo, você deseja depositar algum valor para começar a realizar transações? Caso positivo, digite (sim), caso não, digite (sair) para cancelar a operação!): ").lower()
        while True:
            if primeiro_deposito == "sim":
                valor_deposito = float(input("Informe qual o valor que você deseja depositar: "))
                if valor_deposito <= 0:
                     print("Não foi possível efetuar o deposito, o valor de deposito deve ser maior que 0!\n")
                     continue
                saldo += valor_deposito
                extrato.append({"Depósito: R$": valor_deposito})
                print("Obrigado pela preferência! Agora você pode utilizar os nossos serviços, segue abaixo o menu com as opções:\n")
                break
            elif primeiro_deposito == "sair":
                print("Obrigado por utilizar nossos serviços!")
                exit()
            else:
                print("Resposta inválida!")
                while primeiro_deposito != "sim" and primeiro_deposito != "sair":
                    primeiro_deposito = input("Seja bem-vindo, você deseja depositar algum valor para começar a realizar transações? Caso positivo, digite (sim), caso não, digite (sair) para cancelar a operação!): ").lower()
                    break

def menu():
    global saldo
    global extrato
    while True:
        selecao_opcao = int(input("Informe qual operação você deseja executar:\n"
        "1(extrato)\n" 
        "2(sacar)\n" 
        "3(transferencia)\n"
        "4(saldo)\n" 
        "5(deposito)\n"  
        "6(sair)\n"))
        if selecao_opcao == 1:
            for e in extrato:
              print(e)
        elif selecao_opcao == 2:
                saque = float(input("Informe o valor que você deseja sacar: "))
                if saldo <= 0:
                  print("Você não possui saldo na conta!")
                elif saque > saldo:
                  print("Você não possui saldo suficiente!")
                else:
                  saldo -= saque
                  print("Você sacou: ", "R$", saque)
                  print("Seu novo saldo após o saque é de: ", "R$", saldo)
                  extrato.append({"Saque: R$": saque})
        elif selecao_opcao == 3:
                    while True:
                        conta_transferencia = input("Qual o número da conta de destino para envio do valor?(preencha com os 9 digitos e sem o hifen (-)): ")
                        if len(conta_transferencia) == 9 and conta_transferencia.isdigit():
                                print("Conta válida!")
                                break
                        else:
                                print("Conta inválida, verifique e tente novamente!")
                    valor_transferencia = float(input("Quanto você deseja transferir?: "))
                    if valor_transferencia < 0:
                            print("Valor inválido para transferência!")
                    elif valor_transferencia > saldo:
                            print("Você não possui saldo suficiente para realizar a transferência!")
                    confirmacao_transferencia = input("Verificou se os dados estão corretos e deseja realmente confirmar a transferência?(sim) para confirmar e (não) para validar novamente:\n").lower()
                    if confirmacao_transferencia == "sim":
                        saldo -= valor_transferencia
                        print("Transação realizada com sucesso para a conta:", conta_transferencia, "\nValor da transferência: ", "R$", valor_transferencia)
                        print("Seu saldo após a transação é de: ", "R$", saldo)
                        extrato.append({"Transferência: R$": valor_transferencia})
                    elif confirmacao_transferencia == "nao" or confirmacao_transferencia == "não":
                        print("Transferência cancelada! Voltando ao menu...")
        elif selecao_opcao == 4:
            print("O seu saldo é: ", "R$", saldo)
        elif selecao_opcao == 5:
          deposito = float(input("Qual valor você deseja depositar?: "))
          if deposito < 0:
                  print("Valor inválido para deposito")
          else:
            saldo += deposito
          print("O seu novo saldo após o deposito é de: ", "R$", saldo)
          extrato.append({"Depósito: R$": deposito})
        elif selecao_opcao == 6:
            print("Obrigado por utilizar nossos serviços!")
            exit()
        else:
            print("Erro: Opção invalida, será necessário recomeçar a operação!")
            break




first_deposito()
menu()