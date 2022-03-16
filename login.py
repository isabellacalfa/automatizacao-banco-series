# coding: utf-8
#! / usr / bin / python

# Projeto de login automático em site

## Bibliotecas:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from configparser import RawConfigParser

## Funções:
def config(filename, section): 
    parser = RawConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db [param [0]] = param [1]
    else:
        raise Exception ('Seção {0} não encontrada no {1} arquivo'.format (section, filename))
    return db

## Variáveis Globais:
site='https://www.bancodeseries.com.br/'
params=config('auth.ini','login')
user=params['user']
passw=params['password']

## Abetura do navegador:
print(f'Iniciando o processo de abertura do navegador...')
options = webdriver.ChromeOptions() # Tratamento de erro
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Tratamento de erro
browser = webdriver.Chrome(options=options) # Tratamento de erro
print(f'Navegador aberto.')

## Acesso ao site de login:
print(f'Iniciando processo de abertura do site {site}...')
browser.get(site) 
print(f'{site} acessado com sucesso.')

## Login:
print(f'Definição dos parâmetros de login...')
username = browser.find_element_by_name('login')
username.send_keys(user)
print(f'Usuário definido. (1/3)')

print(f'Senha definida. (2/3)')

print(f'Botão Logar-se definido. (3/3)')
#login_attempt.submit()
print(f'Login realizado com sucesso.')
time.sleep(10)
#username = browser.find_element_by_id("matinput")
#password = browser.find_element_by_id("password")
#username.send_keys(user)
#password.send_keys(password)
#login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#login_attempt.submit()
#ids = browser.find_elements_by_xpath('//*[@class]')
#for ii in ids:
    #print ii.tag_name
    #print(ii.get_attribute('class'))    # id name as string


## Fechamento do navegador:
print('Navegador fechado.')
#browser.close()
