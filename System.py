from library.Interface import *
from library.arquivo import *
from time import sleep


arq = 'novoarquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

header('SISTEMA ARQUIVO 2.0')
while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        header('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('Saindo do sistema... Até mais!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
