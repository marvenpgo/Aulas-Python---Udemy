num1 = int(input("Digite o primeiro numero: \n"))
num2 = int(input("Digite o segundo numero: \n"))

# Aritméticos

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2   #resto da divisão
exp = num1 ** num2  #exponenciação

# print(f"O resto da divisão entre {num1} e {num2} é {mod}")

# Comparação - retorna booleano

bigger = num1 > num2 
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

# print(f"O numero {num1} é igual a {num2}? {equal}\n")
# print(f"O numero {num1} é maior ou igual a {num2}? {bigger_equal}")

# Atribuição

num1 += 1 # soma 1 ao num1
num1 -= 1 # subtrai 1 do num1
num1 *= 1 # multiplica num1 por 1
num1 /= 1 # divide num1 por 1
