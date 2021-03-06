
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO!: Por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '*' * tam


def header(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    header('MENU PRINCIPAL')
    for c, i in enumerate(lista, start=1):
        print(f"\033[33m{c}\033[m - \033[34m{i}\033[m")
    print(linha())
    return leiaInt('\033[32mSua Opção: \033[m')

