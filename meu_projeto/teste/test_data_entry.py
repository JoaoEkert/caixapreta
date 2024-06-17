from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def teste_entrada_dados():
    driver = webdriver.Chrome()

    # Abrir o sistema web
    driver.get('https://the-internet.herokuapp.com/login')

    # Localizar os campos de login
    campo_usuario = driver.find_element(By.ID, 'username')
    campo_senha = driver.find_element(By.ID, 'password')
    botao_login = driver.find_element(By.XPATH, '//*[@id="login"]/button')

    # Inserir dados válidos
    campo_usuario.send_keys('tomsmith')
    campo_senha.send_keys('SuperSecretPassword!')
    botao_login.click()
    time.sleep(3)

    # Verificar se os dados foram processados corretamente
    assert 'You logged into a secure area!' in driver.page_source

    driver.quit()

if __name__ == "__main__":
    teste_entrada_dados()
