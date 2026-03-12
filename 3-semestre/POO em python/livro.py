class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.livre = True

    def realizar_emprestimo(self):
        if self.livre:
            self.livre = False
            return True
        return False

    def realizar_devolucao(self):
        self.livre = True

    def __str__(self):
        status = "Disponível" if self.livre else "Emprestado"
        return f"'{self.titulo}', de {self.autor} ({self.ano}) - Status: {status}"


class Ebook(Livro):
    def __init__(self, titulo, autor, ano, tamanho_arquivo_mb):
        super().__init__(titulo, autor, ano)
        self.tamanho_arquivo_mb = tamanho_arquivo_mb

    def __str__(self):
        status = "Disponível" if self.livre else "Emprestado"
        return f"'{self.titulo}', de {self.autor} ({self.ano}) [{self.tamanho_arquivo_mb}MB] - Status: {status}"