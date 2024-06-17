import time
from selenium import webdriver

def teste_desempenho():
    driver = webdriver.Chrome()

    # Medir o tempo de carregamento de uma página
    inicio_tempo = time.time()
    driver.get('https://the-internet.herokuapp.com/login')
    fim_tempo = time.time()

    tempo_carregamento = fim_tempo - inicio_tempo
    print(f"Tempo de carregamento: {tempo_carregamento} segundos")

    driver.quit()

if __name__ == "__main__":
    teste_desempenho()
