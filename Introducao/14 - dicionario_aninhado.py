import pprint # modulo para melhorar a visualizaçao do dicionario aninhado

# inserir um dicionario dentro de outro dicionario
# no exemplo, o filme é um dicionario que vai receber os dados dentro dele em outro dicionario

filme_dic = {
    "Armagedon" : {
        "ano" : 1998,
        "nota" : 9,
        "genero" : ["ação", "romance", "drama"] 
    },
    "Matrix" : {
        "ano" : 1995,
        "nota" : 8,
        "genero" : ["ficção", "ação"]
    },
    "Senhor dos Anéis" : {
        "ano" : 2000,
        "nota" : 9.7,
        "genero" : ["fantasia", "ação"]
    }
}
#print(filme_dic)

# usando o pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filme_dic)

# 1 - Buscar informacao dentro de um dicionario aninhado
print(filme_dic["Matrix"]["genero"])

# 2 - Adicionar um novo item
filme_dic["Matrix"]["Ator"] = "Keanu Reaves"
pp.pprint(filme_dic)

# 3 - Exluir um item do dicionario
del filme_dic["Senhor dos Anéis"]
pp.pprint(filme_dic)