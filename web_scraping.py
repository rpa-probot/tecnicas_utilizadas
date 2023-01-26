from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Web Scraping via API's Chrome Web Driver e Selenium

# 1° Realizando atualização automática da API Web Driver (baseada nas atualizações do browser Google Chrome), se necessário;
# 2° Lendo arquivo de credenciais e declarando usuario e senha (de forma segura);
# 3° Declarando dicionário de x-path com as coordenadas a serem utilizadas;
# 4° Alterando frame da tela para ter acesso ao conteúdo clicável;
# 5° Ordenar ao navegador que aguarde a presença de um elemento, cujo coordenada foi repassada, para que prossiga;
# 6° Após o elemento ser completamente recarregado em tela, ordenamos que o navegador o procure e tome a decisão cabível;
# 7° Realiza sua tarefa principal, retorna para o frame anterior, realiza logout e encerra a sessão do browser.


def web_scraping():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    navegador = driver
    navegador.get('https://LINK_DO_SITE')
    navegador.maximize_window()
    
    credenciais = open('C:\\CAMINHO_ARQUIVO_CREDENCIAIS.txt', 'r')
    chaves = credenciais.readlines()
    credenciais.close()

    usuario = chaves[0][:-1]
    senha = chaves[1]


    dict_xpath = {

                'usuario': '//*[@id="INPUT USUARIO"]',
                'senha': '//*[@id="INPUT SENHA"]',
                'login': '//*[@id="BUTTON LOGIN"]',
                'download': '//*[@id="BUTTON DOWNLOAD"',
                'logout': '//*[@id="BUTTON LOGOUT"]'

    }


    main_frame = navegador.find_element(By.NAME, 'main')
    navegador.switch_to.frame(main_frame)

    WebDriverWait(navegador, timeout=120).until(EC.presence_of_element_located((By.XPATH, dict_xpath['usuario'])))
    navegador.find_element(By.XPATH, dict_xpath['usuario']).click()
    navegador.find_element_by_xpath(dict_xpath['usuario']).send_keys(usuario)

    WebDriverWait(navegador, timeout=120).until(EC.presence_of_element_located((By.XPATH, dict_xpath['senha'])))
    navegador.find_element(By.XPATH, dict_xpath['senha']).click()
    navegador.find_element_by_xpath(dict_xpath['senha']).send_keys(senha)

    WebDriverWait(navegador, timeout=120).until(EC.presence_of_element_located((By.XPATH, dict_xpath['login'])))
    navegador.find_element(By.XPATH, dict_xpath['login']).click()

    ################ CONTEÚDO GENÊRICO ###############

    WebDriverWait(navegador, timeout=120).until(EC.presence_of_element_located((By.XPATH, dict_xpath['download'])))
    navegador.find_element(By.XPATH, dict_xpath['download']).click()

    #################################################

    navegador.switch_to.default_content()

    WebDriverWait(navegador, timeout=120).until(EC.presence_of_element_located((By.XPATH, dict_xpath['logout'])))
    navegador.find_element(By.XPATH, dict_xpath['logout']).click()

    navegador.close()
    navegador.quit()
