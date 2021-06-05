class Book:
    def __init__(self, titulo, autor, paginas):
        print('Livro criado!')
        self.titulo = titulo
        self.autor = autor
        self.paginas = int(paginas)

    def __str__(self):
        return f'Título: {self.titulo}, autor: {self.autor} e número de páginas: {self.paginas}.'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Livro excluído!')


livro2 = Book('Work 4 hour work week', 'Tim Ferris', 217)
print(livro2)
print(len(livro2))
del livro2