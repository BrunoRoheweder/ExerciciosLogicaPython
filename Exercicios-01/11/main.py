# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo. 


num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = float(input("Numero 3: "))


op1 = (num1*2)+(num2/2)
op2 = (num1*3)+num3
op3 = num3**3

print(op1)
print(op2)
print(op3)