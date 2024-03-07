from selenium import webdriver
from selenium.webdriver.common.by import By
from config import Excel, config_navegador
from time import sleep
import os

def inicar_scraping():

    #Excel --------------------------------------------------------------------------------
    excel = Excel()
    excel.style_excel()
    excel.config_excel()

    #WebScraping
    navegador = config_navegador()

    def buscar_tefone(link):
        opcoes = webdriver.ChromeOptions()
        opcoes.add_experimental_option('detach', True)
        opcoes.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        navTelefone = webdriver.Chrome(options=opcoes)
        navTelefone.get(f'{link}')

        sleep(3)
        telefone_link = navTelefone.find_element(By.XPATH, '//*[@data-patient-app-event-name="dp-call-phone"]').get_attribute('href')
        telefone_number = telefone_link[4:]
        sleep(3)

        navTelefone.quit()

        return telefone_number

    i = 1
    stop = False
    quantidade_psicologos = '<Digite aqui a quantidade de psicologos que deseja buscar>'

    while True:
        sleep(3)
        div_mae = navegador.find_element(By.XPATH, '//*[@id="search-content"]/ul')
        div_lists = div_mae.find_elements(By.CLASS_NAME, 'has-cal-active')

        for lista in div_lists:

            if i > quantidade_psicologos:
                stop = True
                break

            nomeGeral = lista.find_element(By.TAG_NAME, 'h3').text
            endereco = lista.find_element(By.CLASS_NAME, 'text-truncate').text
            telefone_link = lista.find_element(By.CLASS_NAME, 'text-body').get_attribute('href')
            
            telefone = buscar_tefone(telefone_link)
            
            excel.transferir_excel(nomeGeral, endereco, telefone)
            
            print(f'Nome do Psicologo: {nomeGeral}') 
            print(f'Endereço: {endereco}')
            print(f'Telefone: {telefone}')
            print(f'Item de número: {i}')
            print('-------------------------------------------------------------------------------------\n')

            i += 1

        if stop == True:
            break
        else:    
            sleep(2)
            btn_next = navegador.find_element(By.CLASS_NAME, 'page-link-next').get_attribute('href')
            navegador.get(f'{btn_next}')
            sleep(6)

    print('\n----------------------------------')
    print('Scraping Finalizado!')
    print(f'Total de itens coletados: {i}')
    print('\nAbrindo Arquivo Excel.........')
    sleep(4)

    os.startfile('<caminho do arquivo excel>')

