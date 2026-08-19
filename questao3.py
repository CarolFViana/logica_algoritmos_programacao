#3. Mini Calculadora. Crie uma mini calculadora que permita ao usuário escolher
#entre as operações de soma, subtração, multiplicação e divisão. Peça dois
#números e a operação desejada. Imprima o resultado.

print("Mini Calculadora")

numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada (+,-,*,/): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado: ", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado: ", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado: ", resultado)
elif operacao == "/":
    if numero2 == 0:
        print("Não é possivel dividir por zero.")
    else:
        resultado = numero1 / numero2
        print("Resultado: ", resultado)
else:
    print("Operação inválida.")