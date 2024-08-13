# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7 

altura = float(input("Altura: "))
sexo = input("Sexo: ")

if sexo == "masculino" and "Masculino":
    homens = (72.7*altura) - 58
    print(f"Para o sexo masculino o peso ideal é {homens}")

elif sexo == "feminino" and "Feminino":
    mulher = (62.1*altura) - 44.7
    print(f"Para o sexo feminino o peso ideal é {mulher}")

else:
    print(f"O Sexo {sexo} é invalido!")