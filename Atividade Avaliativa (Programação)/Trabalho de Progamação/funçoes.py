import time

def registrar(biblioteca):

    while True:
        print("Quando terminar adicionar os liveos, pode digitar 'sair'.")
        livro = input("Qual nome do livro que deseja registrar?: ")
        if livro.lower() == "sair":
            break
        biblioteca.append(livro)
        print(f"O livro '{livro}' foi adicionado com sucesso na biblioteca")
    
    return biblioteca


def pegar_livro(biblioteca, pegados):
    print(biblioteca)
    selecionar = input("Fale num do livros:")
    if selecionar in biblioteca:
        biblioteca.remove(selecionar)
        pegados.append(selecionar)
        print(f"O livro '{selecionar}' foi pego com sucesso")
    else:
        print(f"O livro '{selecionar}' que voce procura, nao tem na biblioteca.")
    
    


def ler_livro(pegados):
    ler = input("Qual livros você deseja ler?: ")
    if ler in pegados:
       print("Boa leitura.")
    else:
       print("Ainda você não pegou esse livro.")


def devolver_livro(pegados, biblioteca):
    devolver = input("Deseja devolver qual livro: ")
    if devolver in pegados:
        pegados.remove(devolver)
        biblioteca.append(devolver)
        print(f"O livro '{devolver}' foi delvovido com sucesso.")
    else:
        print(f"Este livro não é da nossa biblioteca.")

    

def verificar_livros(pegados, biblioteca): 
    print(F"Verificando se livros estão na biblioteca...")
    time.sleep(0.60)
    print(f"Os livros que foram pegados foram: {pegados}")
    print(f"Os livros que continua na biblioteca são: {biblioteca}")

