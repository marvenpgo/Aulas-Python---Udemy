# 1 - listando valores de 0 a 10 que sejam menores que 4.
# usando FOR ficaria assim:
# for i in range(10):
#   if i < 4:
#       print(i)

# usando list comprehension
# cria um variavel que recebe o list - tudo numa linha
# o FOR anterior com o IF na mesma linha
listnumbers = [i for i in range(10) if i < 4]

print(listnumbers)


# 2 - buscar filmes que possuem a letra "i" no titulo
filmes = ["Matrix", "Titanic", "Armagedon", "Ultimo Samurai", "Platoon", "Titaball"]

filmeswithI = [movie for movie in filmes if 'i' in movie.lower()]

print(filmeswithI)

# 3 - listar os filmes, menos o filme indicado
filmesWatched = [movie for movie in filmes if movie != "Titanic"]
print(filmesWatched)

# 4 - encontrando um filme pelo nome
while True:    # loop enquanto for verdadeiro - quebra o loop com sair = break
    searchName = input("Digite o filme para buscar na lista, ou sair para encerrar: ")
    if searchName.lower() == 'sair':
        print("Programa encerrado.")
        break

    moviefound = [movie for movie in filmes if searchName.lower() in movie.lower()]
    if moviefound:
        print(f"Filme(s) encontrado(s) com {searchName}: ")
        for m in moviefound:
            print(m)
    else:
        print(f"Nenhum filme encontrato com o nome {searchName}. Tente novamente.")