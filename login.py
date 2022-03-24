# coding: utf-8
#! / usr / bin / python

# Projeto de login automático em site

## Bibliotecas:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from configparser import RawConfigParser
from datetime import datetime

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
#Pasta com o executável do chromedriver.exe:
executable_path=params['executable_path'] 
#Pasta com o adblock:
path_to_extension = r'C:\Users\Isabella Calfa\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.44.0_0'

## Abertura do navegador:
inicio=datetime.now()
print(f'Iniciando o processo de abertura do navegador...')
### Tratamento de Erros:
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('load-extension=' + path_to_extension)
### Acesso ao navegador:
try:
    browser = webdriver.Chrome(options=options)
except:
    browser = webdriver.Chrome(options=options,executable_path=executable_path)
fim=datetime.now()
print(f'Navegador aberto. Tempo de Execução: {fim-inicio}.')

## Acesso ao site de login:
inicio=datetime.now()
print(f'Iniciando processo de abertura do site {site}...')
browser.get(site) 
fim=datetime.now()
print(f'{site} acessado com sucesso. Tempo de Execução: {fim-inicio}.')

## Login:
inicio=datetime.now()
### Abertura da tela de login:
try:
    browser.find_element_by_link_text('Login').click()
except:
    print(f'ERRO! Botão de login não pressionado.')    
print(f'Definição dos parâmetros de login...')
### Definição de usuário:
print("Elemento de login está visível? " + str(browser.find_element_by_name('login').is_displayed()))
browser.find_element_by_name('login').send_keys(user)
### Definição de senha:
#browser.find_element_by_name('pw').send_keys(passw)
### Selecionando o botão de login:
#try:
#    browser.find_element_by_css_selector('btn btn-primary').click()
#    inicio=datetime.now()
#    print(f'Login realizado com sucesso. Tempo de Execução: {fim-inicio}.')
#except:
#    print(f'ERRO! Botão de login não identificado.')
#time.sleep(10)

## Fechamento do navegador:
x=input('Continuar:')