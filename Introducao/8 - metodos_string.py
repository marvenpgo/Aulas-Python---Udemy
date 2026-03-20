movieName = "Top Gun"
movieDescription = '''
    Top Gun Maverick, é um filme de aviação e aventura,
    muito consagrado na indústria cinematográfica
'''

# Deixar tudo em maiusculo
print(movieName.upper())

# Deixar tudo em minusculo
print(movieName.lower())

# Primeira letra em maiusculo
print(movieName.capitalize())

# Cada palavra em maiusculo
print(movieName.title())

# Retornar string centraliza com preenchimento
print(movieName.center(10, '-'))

# Trazer a posição de um determinado caracter
print(movieName.find('u'))

# Mostrar a contagem de caracteres
print(len(movieName))

# Alterar elemento por outro
print(movieName.replace("Top", "Matrix"))

# Quebrar a string em partes, separadas por virgula
print(movieDescription.split(','))