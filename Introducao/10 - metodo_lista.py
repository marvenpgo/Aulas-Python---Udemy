filmes = ["Interestelar", "Armagedon", "Matrix", "Ultimo Samurai", "Top Gun"]

# 1 - Tamanho da lista
print(len(filmes))

# 2 - Recuperar indice do item da lista pelo nome
print(filmes.index("Matrix"))

# 3 - Adicionar um item ao final da lista
filmes.append("Senhor dos Anéis")
print(filmes)

# 4 - Ordenar a lista
filmes.sort()
print(filmes)

# 5 - Copiar os itens de uma lista para outra.
filmes_lista = filmes.copy()
print(filmes_lista)

# 6 - Remover um item da lista pelo nome
filmes.remove("Matrix")
print(filmes)

# 7 - Remover todos os itens da lista
filmes.clear()
print(filmes)