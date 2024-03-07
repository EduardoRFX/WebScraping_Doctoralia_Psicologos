from scrappy import inicar_scraping
from time import sleep

def menu():
    print('\n----------Scraping Doctoralia----------\n')
    print('1. Inicar')
    print('2. Como funciona o WebScraper')
    print('3. Sair')
    escolha = input('\nPor favor, digite uma opção: ')

    return escolha


def main():
    while True:
        opcao = menu()

        if opcao == '1':
            inicar_scraping()

        elif opcao == '2':
            print('\nO Scrapping busca por meios automaticos(Robores automatizados)\na extração de dados especificos de um determinado site.')

        elif opcao == '3':
            print('\nFinalizando o Serviço......')
            sleep(3)
            break
        
        else:
            print('\nOpcão invalida! Por favor digite novamente.')

main()