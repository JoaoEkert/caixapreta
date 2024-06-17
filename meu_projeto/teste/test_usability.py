from selenium import webdriver
from selenium.webdriver.common.by import By

def teste_usabilidade():
    driver = webdriver.Chrome()

    # Abrir o sistema web
    driver.get('https://the-internet.herokuapp.com/login')

    # Verificar a presença de elementos-chave
    assert driver.find_element(By.ID, 'username')
    assert driver.find_element(By.ID, 'password')
    assert driver.find_element(By.XPATH, '//*[@id="login"]/button')

    driver.quit()

if __name__ == "__main__":
    teste_usabilidade()
