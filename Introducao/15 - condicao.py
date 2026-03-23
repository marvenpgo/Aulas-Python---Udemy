# Informações do filme

# nome = input("Digite o nome do filme: \n")
# ano = int(input("Digite o ano de lançamento: \n"))
# nota = float(input("Digite a nota de avaliação: \n"))

# # Verifica se o filme é recomendado
# if nota > 8.0 and ano > 2015:
#     print(f"O filme {nome} é muito bom. Recomendo que assista")
# else:
#     print(f"O filme {nome} ainda não atingiu uma boa nota.")

########## usando ELIF #################################

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operacao = input("Informe qual operaçao ( + - * / ): ")

if num1 or num2:
    if operacao == "+":
        resultado = num1 + num2
        print(f"O resultado da soma de {num1} e {num2} é {resultado}\n")
    elif operacao == "-":
        resultado = num1 - num2
        print(f"O resultado da subtração de {num1} - {num2} é {resultado}\n")
    elif operacao == "*":
        resultado = num1 * num2
        print(f"O resultado da multiplicação entre {num1} X {num2} é {resultado}")
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão de {num1} por {num2} é {resultado}")
        else:
            print("Erro: Divisão por zero.")
            print("O resultado é Zero.")
    else:
        print("Operação inválida.")
else:
    print("Um dos números digitados é inválido.")