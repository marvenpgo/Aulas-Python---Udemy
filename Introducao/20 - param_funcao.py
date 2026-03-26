# 1 - função imprime um nome completo
def nome_full(primeiro_nome,ultimo_nome):
    print(f"O nome é {primeiro_nome} {ultimo_nome}")

nome_full("Marcelo", "Venancio")

# 2 - função para somar dois numeros
def soma(num1, num2):
    total = num1 + num2
    return total

numero1 = float(input("Informe o primeiro numero: "))
numero2 = float(input("Informe o segundo número: "))

print(f"A soma de {numero1:.2f} + {numero2:.2f} é {soma(numero1, numero2):.2f}")

# 3 - função com parametro default
def pais(country="Brasil"):
    print(f"Eu moro em: {country}")

pais()  # vai retornar o default

pais("Inglaterra")   # vai retornar o valor informado.

# 4 - função para avaliar um filme
def avalia_filme(num_aval, nome_filme):
    total = 0
    for i in range(num_aval):
        nota = float(input("Digite a nota para o filme: "))
        total += nota
    
    if num_aval > 0:
        media = total / num_aval
    else:
        media = 0

    print(f"A média de avaliação do filme {nome_filme} é {media:.2f}")

avalia_filme(3, "Matrix")
