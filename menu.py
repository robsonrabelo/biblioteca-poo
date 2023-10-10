from livro.livro_fisico import LivroFisico
from socio.socio import Socio
from biblioteca.biblioteca import Biblioteca

biblioteca = Biblioteca()
socio = Socio("Francisco", "85996906200", "Av. A, 110")

def criarLivro(titulo, autor, ano_publi, num_pag):
    livro = LivroFisico(titulo, autor, ano_publi, num_pag)
    return livro

while True:
    print("Bem vindo ao menu --")
    print("1 - Adicionar Livro")
    print("2 - Remover Livro")
    print("3 - Adicionar Socio")
    print("4 - Remover Socio")
    print("5 - Aluguar Livro")
    print("6 - Devolver Livro")
    print("7 - Listar Livro")
    print("8 - Listar Socios")
    opcao = int(input('Selecione a opção: '))
    if opcao == 1:
        titulo = input('Digite o titulo: ')
        autor = input('Digite o autor: ')
        ano = input('Digite o ano:')
        num_pages = int(input('Digite o número de paginas'))
        livro = criarLivro(titulo, autor, ano, num_pages)
        biblioteca.adicionarLivro(livro)
    elif opcao == 2:
        id = input('Digite o ID do livro: ')
        if biblioteca.removerLivro(id):
            print("Livro removido com sucesso!")
        else:
            print("Livro não encontrado!")
    elif opcao == 3:
        nome = input('Digite o nome do socio: ')
        telefone = input('Digite o telefone: ')
        endereco = input('Digite o endereço: ')
        socio_novo = Socio(nome, telefone, endereco)
        biblioteca.adicionarSocio(socio_novo)
    elif opcao == 4:
        id = input('Digite o ID do socio: ')
        if biblioteca.removerSocio(id):
            print('Socio removido com sucesso!')
        else:
            print('Socio não encontrado!')
    elif opcao == 5:
        print("Em desenvolvimento!")
    elif opcao == 6:
        print("Em desenvolvimento!")
    elif opcao == 7:
        biblioteca.listarLivros()
    elif opcao == 8:
        biblioteca.listarSocios()