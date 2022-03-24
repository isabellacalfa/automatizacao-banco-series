# Projeto de automatização de funções em site

**Projeto em desenvolvimento**

**Site:** https://www.bancodeseries.com.br/.

## 1. Pré-Requisitos:
O projeto foi realizado utilizando o navegador Google Chrome, mas pode ser aplicado em outros navegadores após ajustes no driver utilizado e funções.
A automatização do site conta com a utilização de um adblock para o navegador. Caso não tenha instalado, é recomendável que faça a instalação antes de aplicar o projeto. A identificação da pasta da extensão é fundamental para a continuidade do código. Para dúvidas sobre como encontrar a pasta do adblock, consulte esse [link](https://www.reddit.com/r/learnpython/comments/4zzn69/how_do_i_get_adblockplus_to_work_with_selenium/).

## 2. Preparação:
### 2.1 Bibliotecas:
Antes de executar o código, é necessário garantir que as bibliotecas necessárias estejam instaladas (*! pip install*) e é preciso que o *chromedriver.exe* (da bib **webdriver**) esteja incluído no PATH do sistema (no PC: Editar Variáveis de Ambiente > Variáveis de Ambiente ... > Path > Editar).

### 2.2 Arquivo auth.ini:
O arquivo auth.ini deve ser no seguinte formato:

[login]<br/>
user=you username<br/>
password=your password<br/>
executable_path=caminho da pasta com o chromedriver.exe<br/>
path_to_extension=caminho da pasta do adblock