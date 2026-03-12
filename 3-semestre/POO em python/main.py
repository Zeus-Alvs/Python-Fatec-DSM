import time
from biblioteca import GestaoBiblioteca
from livro import Livro, Ebook
from usuario import Cliente

sistema = GestaoBiblioteca()

while True:
    print("\n" + "="*30)
    print("      MENU DA BIBLIOTECA      ")
    print("="*30)
    print("1 - Cadastrar livro físico")
    print("2 - Cadastrar livro digital (Ebook)")
    print("3 - Cadastrar novo cliente")
    print("4 - Registrar empréstimo")
    print("5 - Registrar devolução")
    print("6 - Ver obras disponíveis")
    print("7 - Ver obras emprestadas")
    print("8 - Encerrar sistema")
    
    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            titulo = input("Informe o Título: ")
            autor = input("Informe o Autor: ")
            ano = int(input("Ano de publicação: "))
            nova_obra = Livro(titulo, autor, ano)
            sistema.registrar_obra(nova_obra)
            print("-- Livro físico registrado!")
            time.sleep(2)

        case 2:
            titulo = input("Informe o Título: ")
            autor = input("Informe o Autor: ")
            ano = int(input("Ano de publicação: "))
            tamanho = float(input("Tamanho do arquivo (em MB): "))
            novo_ebook = Ebook(titulo, autor, ano, tamanho)
            sistema.registrar_obra(novo_ebook)
            print("-- Ebook registrado!")
            time.sleep(2)

        case 3:
            nome = input("Nome completo do cliente: ")
            codigo = input("Código de identificação: ")
            novo_cliente = Cliente(nome, codigo)
            sistema.registrar_cliente(novo_cliente)
            print("-- Cliente registrado com sucesso!")
            time.sleep(2)

        case 4:
            codigo = input("Código do cliente: ")
            titulo = input("Título da obra: ")
            
            cliente_encontrado = sistema.localizar_cliente(codigo)
            obra_encontrada = sistema.localizar_obra(titulo)

            if not cliente_encontrado:
                print("-- Erro: Cliente não localizado no sistema.")
                time.sleep(2)
            elif not obra_encontrada:
                print("-- Erro: Obra não localizada no catálogo.")
                time.sleep(2)
            else:
                cliente_encontrado.solicitar_livro(obra_encontrada)
                time.sleep(2)

        case 5:
            codigo = input("Código do cliente: ")
            titulo = input("Título da obra: ")
            
            cliente_encontrado = sistema.localizar_cliente(codigo)
            obra_encontrada = sistema.localizar_obra(titulo)

            if not cliente_encontrado:
                print("-- Erro: Cliente não localizado.")
                time.sleep(2)
            elif not obra_encontrada:
                print("-- Erro: Obra não localizada.")
                time.sleep(2)
            else:
                cliente_encontrado.entregar_livro(obra_encontrada)
                time.sleep(2)

        case 6:
            sistema.exibir_disponiveis()
            time.sleep(2)

        case 7:
            sistema.exibir_emprestados()
            time.sleep(2)

        case 8:
            print("Encerrando o sistema.")
            time.sleep(2)
            break

        case _:
            print("-- Opção inválida! Tente novamente.")
            time.sleep(2)