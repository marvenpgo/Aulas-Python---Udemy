# função recursiva é uma função que chama ela mesma

"""
Fatorial de um número = multiplicação de um número -1 até o um
Ex: fatorial de 5: 5 * 4 * 3 * 2 * 1

"""

# 1 - Fatorial de um numero
def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))

numero = int(input("Digite o numero para o fatorial: "))

print(f"O fatorial de {numero} é {fatorial(numero)}")

# 2 - Soma total de um número (mesma ideia do fatorial)
def total_soma(num):
    if num == 1:
        return 1
    else:
        return (num + total_soma(num - 1))
    
numero_soma = int(input("Digite o numero para somar: "))
print(f"A soma de {numero_soma} é {total_soma(numero_soma)}")