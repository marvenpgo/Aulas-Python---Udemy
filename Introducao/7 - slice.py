movieName = "Top Gun"
# string[início : fim] - índice começa na posição zero e termina em índice final -1

# 1 - buscar toda a string a partir da primeira posição
print(movieName[0:])   # a partir da posição até o final

# 2 - buscar toda string até a ultima posição
print(movieName[:7])   # posiçao final é 6

# 3 - buscar toda string da terceira até a última posição
print(movieName[2:])

'''
string[início:fim:passo] - 
índice começa na posição zero e termina em índice final -1
passo = determina o incremento. Por padrão esse número é 1
'''
# 4 - buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - buscar toda a string nos indices impares de 2 em 2
print(movieName[1::2])

# 6 - inverter uma string de traz pra frente
print(movieName[::-1])