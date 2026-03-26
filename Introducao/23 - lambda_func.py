# função lambda também conhecida como função anônima.
# recebe uma variável

# 1 - função de potencia de um número
power = lambda num: num ** 2  # num elevado a segunda potencia
print(power(5))
print(power(9))

# 2 - função que verifica se um número é par
par_impar = lambda x: x % 2 == 0  # se o resto da divisão por 2 = 0 é par
print(par_impar(27))
print(par_impar(36))

# 3 - função que divide um número por outro
divi = lambda x, y: x / y 
print(divi(30, 3))

# 4 - função que inverte uma string
invert = lambda s: s[::-1]
print(invert("olecraM"))

# 5 - funcionalidades relacionadas aos filmes
movie_list = ["Matrix", "Platoon", "Armagedon", "Titanic", "Jurassic Park"]
notas = {
    "Matrix": [8.5, 9, 7.8],
    "Platoon": [9.3,8.8,9.1],
    "Armagedon": [8.7,8.9,9.1],
    "Titanic": [9.7,9.2,8.8],
    "Jurassic Park": [9.3,8.7,9.1]
}

# função para calcular a média de avaliações de um filme
media_notas = lambda movie_name: (sum(notas[movie_name]) / len(notas[movie_name]))

print(f"A média de avaliações para o filme Matrix é {media_notas("Matrix"):.2f}")

# função que verifica se um filme está na lista
found = lambda movie_name: movie_name in movie_list
print(found("Platoon"))

# função para recomendar um filme com base na avalição média
recomend = lambda movie_name: f"Recomendo assistir {movie_name} com média de {media_notas(movie_name):.2f}"
print(recomend("Titanic"))