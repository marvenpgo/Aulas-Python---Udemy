# lista de filmes
filmes = ["Matrix", "Titanic", "Armagedon", "Ultimo Samurai", "Platoon"]

# 1 - iterando valores de uma lista
for movie in filmes:
    print(movie)

# 2 - quando a condicao for atendia, o loop será encerrado
for movie in filmes:
    if movie == "Ultimo Samurai":
        break
    print(movie)

# 3 - quando a condicao for atendida, o loop irá para a próxima iteração
for movie in filmes:
    if movie == "Matrix":
        continue
    print(movie)

# 4 - avaliação do filme
filmenome = input("Digite o nome do filme: ")
filmenota = int(input("Digite quantas avaliações deseja fazer: "))

total = 0
for i in range(filmenota):
    nota = float(input("Digite a nota para o filme: "))
    total += nota

if filmenota > 0:
    media = total / filmenota
else:
    media = 0

print(f"A média de avaliacão para o filme {filmenome} é {media:.2f}")