# SET usar {} como um dicionario, porém tem apenas a propriedade de valor
# dicionario tem duas propriedades: chave e valor
filme_set = {"Interestelar", "Armagedon", "Matrix", "Ultimo Samurai", "Top Gun"}
print(filme_set)

# SET tem alguma limitações

# 1 - Buscar o tamanho do set
print(len(filme_set))

# 2 - o valor True e 1 são considerados o mesmo valor
exemplo_set = {"Matrix", True, 8.8, 1}
print(exemplo_set)

# 3 - Adicionar o conteude de outro set (não repete itens iguais)
filme_set.update(exemplo_set)
print(filme_set)

# 4 - Remove item no set
filme_set.remove(True)
filme_set.remove(8.8)
print(filme_set)