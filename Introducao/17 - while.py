# lista de filmes
filmes = ["Matrix", "Titanic", "Armagedon", "Ultimo Samurai", "Platoon"]

# 1- iterando valores de uma lista de filmes usando while
index = 0

while index < len(filmes):
    print(filmes[index])
    index += 1

# 2 - quando a condição for atendida, o loop será encerrado
index = 0

while index < len(filmes):
    if filmes[index] == "Armagedon":
        break
    print(filmes[index])
    index += 1

# 3 - quando a condição for atendida, o loop vai para a próxima iteração
index = 0
while index < len(filmes):
    if filmes[index] == "Armagedon":
        index += 1
        continue
    print(filmes[index])
    index += 1

# 4 - avaliação do filme com While
filmenome = input("Digite o nome do filme: ")
filmenota = int(input("Digite quantas avaliações deseja fazer: "))

total = 0
count = 0

while count < filmenota:
    nota = float(input("Informe a nota para o filme: "))
    total += nota
    count += 1

if filmenota > 0:
    media = total / filmenota
else:
    media = 0

print(f"A média de avaliacão para o filme {filmenome} é {media:.2f}")