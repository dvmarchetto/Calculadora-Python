import os
os.system('cls')

num1 =  float(input("\nDigite o primeiro número:: "))
num2 =  float(input("Digite o segundo número:: "))
operadores = ["+", "-", "*", "/", "**", "//"]

for i, operador in enumerate(operadores, start=1):
    print(f"{i}) {operador}")

op = input("Digite seu operador:: ")

if op not in operadores:
    raise ValueError("Digite um valor válido.")

if num2 == 0 and op == "/":
    raise ZeroDivisionError("Não é possível dividir por 0.")

print("="*100)

match op:
    case "+":
        print(f"o resultado é:",num1 + num2)
    case "-":
        print(f"o resultado é:",num1 - num2)
    case "*":
        print(f"o resultado é:",num1 * num2)
    case "/":
        print(f"o resultado é:",num1 / num2)
    case "**":
        print(f"o resultado é:",num1 ** num2)
    case "//":
        print(f"o resultado é:",num1 // num2)
