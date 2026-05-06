# Desenvolva um programa que simule um caixa eletrônico.
# O sistema deve iniciar com um saldo de R$ 1000,00 e solicitar ao usuário o valor que deseja sacar.
# Após a tentativa de saque, exiba mensagens adequadas informando o resultado da operação e finalize o programa.
# Utilizar a estrutuura de tratamento de erros.

print('=====Novo Saldo=====')


try:
   saldo = 1000
   saque = float(input('Informe o valor do saque: '))
    
except ValueError:
    print('Valor Inválido')
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário')   
else:
    if saque > saldo:
        print('Saldo Insuficiente') 
    elif saque <= 0:
        print('Saque precisa ser maior ou igual a R$ 2,00')
    else:
        saldo -= saque
        print('\nSaque realizado com sucesso')
        print(f'Saldo em conta R$ {saldo:.2f}')
finally:
    print('Operação realizada')

print('\nPrograma Encerrado')

    