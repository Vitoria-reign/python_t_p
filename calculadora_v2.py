saida = ""
#funcoes da operação

def adicao(a, b):
    return a+b
def subtracao(a, b):
    return a-b
def multiplicacao(a, b):
    return a*b
def divisao(a, b):
    return a/b

#criando menu
while saida != "n":
    print("1 - Somar")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisao")
    operacao = int(input("Digite a operação que quer realizar\n"))
    num1 = float(input("Digite o primeiro número: \n"))
    num2 = float(input("Digite o segundo número: \n"))
    if operacao == 1:
        resultado = adicao(num1, num2)
        print("O resultado da adiçõa é: ", resultado)
    elif operacao == 2:
        resultado = subtracao(num1, num2)
        print("O resultado da subtração é: ", resultado)
    elif operacao == 3:
        resultado = multiplicacao(num1, num2)
        print("O resultado da multiplicação é: ", resultado)
    elif operacao == 4:
        if num2 == 0:
            print("O segundo número não pode ser zero \n")
            num2 = float(input("Digite um número válido\n"))
        resultado = divisao(num1, num2)
        print("O resultado da divisão é: ", resultado)
    else:
        print("Opção inválida, escolha um número do menu!")
    saida = str.lower(input("Quer continuar? Digite S ou N:\n "))
print("Você encerrou a operação!")














