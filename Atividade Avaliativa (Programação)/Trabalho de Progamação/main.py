from funçoes import *
from tkinter import *

biblioteca = []
pegados = []

while True:
    print("\nEscolha uma opção:")
    print("1. Pegar livro")
    print("2. Ler livro")
    print("3. Devolver livro")
    print("4. Verificar livros")
    print("5. Registrar livros")
    print("6. Sair")
    opcao = input("Opção: ")
    if opcao == '1':
        pegar_livro(biblioteca, pegados)
    elif opcao == '2':
        ler_livro(pegados)
    elif opcao == '3':
        devolver_livro(pegados, biblioteca)
    elif opcao == '4':
        verificar_livros(pegados, biblioteca)
    elif opcao == '5':
        registrar(biblioteca)
    elif opcao == '6':
        break
    else:
        print("Opção inválida. Tente novamente.")

janela = Tk()


janela = mainloop()