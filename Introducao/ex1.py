# 1 - Escreva um programa que lê dois nomes e retorna uma string 
# formatada no formato "UltimoNome", "PrimeiroNome".

# primeiroNome = input("Digite seu primeiro nome: ")
# ultimoNome = input("Digite seu ultimo nome: ")

# nomeFormatado = f"{ultimoNome} {primeiroNome}"

# print(ultimoNome, primeiroNome)
# print(nomeFormatado)
# =============================================================================================================
# 2 - Inverta a ordem das palavras de uma string fornecida

# texto = "Python é muito interessante"
# palavras =  texto.split()   # quebra o texto em uma lista de palavras
# textoInvertido = " ".join(palavras[::-1])   # join concatena numa string / split -1 inverte a ordem
# print(palavras)
# print(textoInvertido)

# ============================================================================================================
# 3 - Verifique se uma string fornecida é um palíndromo (pode ser lida de traz pra frente e vice versa)

texto1 = "arara"
texto2 = "python"

# normalizar o texto (tudo minusculo, sem espaços)
texto1_format = texto1.lower().replace(" ","")
texto2_format = texto2.lower().replace(" ","")

# verifica se o texto original é igual ao ser reverso
palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)