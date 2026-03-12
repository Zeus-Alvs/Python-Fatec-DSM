class GestaoBiblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def registrar_obra(self, obra):
        self.catalogo.append(obra)

    def registrar_cliente(self, cliente):
        self.membros.append(cliente)

    def localizar_cliente(self, codigo_busca):
        for cliente in self.membros:
            if cliente.codigo == codigo_busca:
                return cliente
        return None

    def localizar_obra(self, titulo_busca):
        for obra in self.catalogo:
            if obra.titulo.lower() == titulo_busca.lower():
                return obra
        return None

    def exibir_disponiveis(self):
        print("\n--- Obras Disponíveis no Acervo ---")
        achou = False
        for obra in self.catalogo:
            if obra.livre:
                print(obra)
                achou = True
        if not achou:
            print("Tudo emprestado no momento.")

    def exibir_emprestados(self):
        print("\n--- Obras Atualmente Emprestadas ---")
        achou = False
        for obra in self.catalogo:
            if not obra.livre:
                print(obra)
                achou = True
        if not achou:
            print("Nenhuma obra emprestada.")