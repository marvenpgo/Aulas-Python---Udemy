name = input("Informe o nome do filme: \n")
yearLaunch = int(input("Digite o ano de lançamento: \n"))
noteMovie = float(input("Informe a nova da avaliação: \n"))

print("Dados do Filme")
print("===============================")
# Alternativa 1 - simples
# print("Nome do Filme",name)
# print("Ano de Lançamento: ",yearLaunch)
# print("Nota do Filme: ",noteMovie)

# Alternativa 2 - na mesma linha de comando
#print("\nNome do Filme:", name, "\nAno de Lançamento: ", yearLaunch, "\nNota do Filme: ", noteMovie)

# Alternativa 3 - usando f string
print(f"\nNome do Filme: {name}\n"
      f"Ano de Lançamento: {yearLaunch}\n"
      f"Nota do Filme: {noteMovie}")