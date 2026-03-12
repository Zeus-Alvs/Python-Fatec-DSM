class Cliente:
    def __init__(self, nome_completo, codigo):
        self.nome_completo = nome_completo
        self.codigo = codigo
        self.historico_emprestimos = []

    def solicitar_livro(self, obra):
        if obra.realizar_emprestimo():
            self.historico_emprestimos.append(obra)
            print("-- Empréstimo concluído com sucesso!")
        else:
            print("-- Atenção: Obra indisponível no momento.")

    def entregar_livro(self, obra):
        if obra in self.historico_emprestimos:
            obra.realizar_devolucao()
            self.historico_emprestimos.remove(obra)
            print("-- Devolução concluída com sucesso!")
        else:
            print("-- Este cliente não está com este livro.")

    def mostrar_livros_retirados(self):
        if not self.historico_emprestimos:
            print("Nenhum empréstimo ativo no momento.")
            return

        print("Livros com o cliente:")
        for obra in self.historico_emprestimos:
            print(f"- {obra.titulo}")

    def __str__(self):
        return f"Cliente: {self.nome_completo} | Código: {self.codigo}"