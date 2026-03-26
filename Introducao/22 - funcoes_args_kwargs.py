"""
    *args - é utilizado quando não temos a certeza de quantos argumentos teremos na função
    - os argumentos são passados como uma tupla

    **kwargs - além dos valores podemos passar as respectivas chaves para cada argumento
    - os argumentos são passados com o um dicionário
"""

# 1 - soma de numeros
def soma(*num):  # o asterisco no parametro indica um valor dinâmico
    soma_total = 0
    for n in num:
        soma_total += n
    print(f"Soma total é {soma_total}")

soma(10,20,30, 50, 120)

# 2 - apresentação de cursos
def presentation(**data): 
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista de cursos: ")
presentation(name="Python", category="Backend", level="iniciante")
presentation(name="Visão Computacional com Python", category="IA", level="avançado")
presentation(name="Dashboards", category="Data Science", level="intermediário")