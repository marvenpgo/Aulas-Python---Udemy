# Python é Case Sensitive
movieName = "Top Gun"
# movieName2 = "top Gun"
# print(movieName == movieName2)  # retorna False

# 1 - String multi-linhas
movieDescription = '''
    Top Gun é um filme de aviação e aventura
    muito consagrado na indústria cinematográfica
'''

# 2 - Multiplicação de Strings
line = "="

print(movieName)
print(line * 52)
print(movieDescription)

# 3 - Procurar uma palavra dentro de um texto

print("Top" in movieName)
print("ação" in movieName)