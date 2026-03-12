import time

i = 0
lista = {}
while i == 0:
    num = int(input("(1)Cadastrar/Atualizar um contato\n(2)Buscar um contato\n(3)Excluir um contato\n(4)Listar todos contatos\n(5)Sair\nEntre: "))
    match num:
        case 1:
            nome = input("Digite o nome: ")
            numero = int(input("Digite o numero de telefone: "))
            if nome in lista:
                j = int(input("Contato existente. Atualizar?(1)sim(0)nao:"))
                if j == 1:
                    lista.update({nome:numero})
                    print("Atualizando contato...")
                    time.sleep(1)
            else:
                lista[nome] = numero
                print("Adicionando contato...")
                time.sleep(1)
        case 2:
            j = input("Digite o nome do contato: ")
            if j in lista:
                print(f"Numero de {j}: {lista[j]}")
            time.sleep(2)
            else:
                print("Contrato nao encontrado.")
                time.sleep(1)
        case 3:
            j = input("Digite o nome do contato: ")
            if j in lista:
                del lista[j]
                print("Excluindo contato...")
                time.sleep(1)
            else:
                print("Nome nao encontrado...")
                time.sleep(1)
        case 4:
            for chave, valor in lista.items():
                print(f'Nome: {chave} - Numero: {valor}')
                time.sleep(2)
        case 5:
            print("Saindo...")
            time.sleep(1)
            i = 1
        case _:
            print("Valor invalido!...")
            time.sleep(1)
    
    