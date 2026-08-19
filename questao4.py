#4. Classificador de Triângulos. Peça ao usuário para digitar o comprimento de três lados de um triângulo. Determine se os lados formam um triângulo válido
#e, em caso afirmativo, classifique-o como Equilátero, Isósceles ou Escaleno.
#Regras:
#a) Para ser um triângulo, a soma de dois lados deve ser maior que o terceiro
#lado (a + b > c, a + c > b, b + c > a).
#b) Equilátero: Todos os três lados são iguais.
#c) Isósceles: Dois lados são iguais.
#d) Escaleno: Todos os três lados são diferentes.

print("Classificador de Triângulos")

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilátero")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")

    else:
        print("Triângulo Escaleno")

else:
    print("Os lados não formam um triângulo.")