# 08. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horaGanha = float(input("Ganho por hora: "))

horaTrabalhada = int(input("Horas trabalhadas no mês: "))

salarioTotal = horaGanha*horaTrabalhada

print(f"Total do salario no mês: {salarioTotal}")