# dicionario permite ter duas propriedades separadas por : (keys : values)
filmes = {
    "titulo" : "Armagedon",
    "ano" : 1998,
    "nota" : 9,
    "genero" : ["ação", "romance", "drama"]   # permite incluir uma lista 
}
print(filmes)

# 1 - Recuperar um elemento do dicionario
print(filmes["genero"])
# ou usa o metodo get - mesmo resultado
print(filmes.get("genero"))

# 2 - Buscar apenas as chaves do dicionario
print(filmes.keys())

# 3 - Buscar apenas os valores do dicionario
print(filmes.values())

# 4 - Buscar itens com chave e valor (retorna uma tupla)
print(filmes.items())

# 5 - Adicionar itens no dicionario
filmes["Ator"] = "Bruce Willis"
print(filmes.items())

# 6 - Atualizar item no dicionario
filmes.update({"nota": 9.5})
print(filmes)

# 7 - Remover item no dicionario
filmes.pop("Ator")
print(filmes)