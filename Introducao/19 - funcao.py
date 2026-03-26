# 1 - função para imprimir uma mensagem
def welcome():
    print("Bem vindo ao sistema de filmes!")

# for i in range(10):  #imprime a funcao dez vezes
#     welcome()

# 2 - função para calcular a média de notas
def media():
    num_avalia = int(input("Digite quantas avaliações deseja fazer: "))
    total = 0
    for i in range(num_avalia):
        nota = float(input("Digite a nota para o filme: "))
        total += nota

    if num_avalia > 0:
        media = total / num_avalia
    else:
        media = 0
    
    return media

print(f"A média das notas é {media():.2f}")

# 3 - função para cadastrar um filme
def cadastrar():
    nome = input("Informe o nome do filme: ")
    ano_lanc = int(input("Digite o ano de lançamento: "))
    preco = float(input("Informe o preço do filme: "))
    nota = float(input("Informe a nota da avaliação: "))
    print(f"{nome} ({ano_lanc}) - R$ {preco:.2f} ")

cadastrar()
cadastrar()