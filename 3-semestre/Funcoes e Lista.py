def eh_primo(num):
    if num <= 1:
        return False
    i = 1
    p = 0
    while i <= num:
        if (num % i) == 0:
            p+=1
        i+=1
    if p <= 2:
        return True
    else:
        return False
    
inicio = int(input("Digite o inicio do intervalo: "))
final = int(input("Digite o fim do intervalo: "))
j = inicio
qtd = 0
maior = inicio
menor = final
while j <= final:
    if eh_primo(j):
        qtd+=1
        if j > maior:
            maior = j
        if j < menor:
            menor = j
    j+=1
if qtd >= 1:
    print(f"{qtd} numeros primos encontrados!")
    print(f"O maior numero primo e {maior}")
    print(f"O menor numero primo e {menor}")
else:
    print("Nenhum numero primo encontrado...")