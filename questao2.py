#Classificador de Idade. Solicite a idade de uma pessoa. Classifique-a como
#"Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso"
#(65 anos ou mais).

print("Classificador de idade")

idade = int(input("Digite a sua idade: "))

if idade < 0 or idade > 130:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 64:
    print("Adulto")
else:
    print("Idoso")