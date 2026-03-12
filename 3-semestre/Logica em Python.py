nome = input("Qual o seu nome? ")
i = 1
peso = 0
mochila = " "
while i == 1:
    item =  input("Digite o nome do item: ")
    kg = int(input("Digite o peso do item: "))
    if kg <= (20 - peso):
        peso += kg
        mochila = mochila + " - " + item
        print("item guardado na mochila")
    else:
        print("Nao cabe, muito pesado.")
    i = 2
    while i < 0 or i > 1: 
        i = int(input("Continuar?(1)Sim - (0)Nao: "))
print("Nome: " + nome)
print(f"Peso usado: {peso}kg")
print(f"Peso restante: {20 - peso}kg")
print("Itens:" + mochila + " - ")