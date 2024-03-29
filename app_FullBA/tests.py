import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# class TestFullBA(LiveServerTestCase):

    def test_home(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/")
        time.sleep(5)
        driver.quit()

<<<<<<< HEAD
    def test_gyms(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/academias/")
        time.sleep(5)
        driver.quit()


    def test_Biceps_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Bíceps")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_B_Rosca_Barra(self):
        driver = webdriver.Chrome(options=chrome_options)
        
        driver.get("http://127.0.0.1:8000/biceps_rosca_com_barra/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_B_Rosca_Apoiada(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/biceps_rosca_apoiada/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()


    def test_B_Rosca_Martelo(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/biceps_rosca_martelo/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()


    def test_B_Rosca_Unilateral(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/biceps_rosca_unilateral/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        driver.quit()

    def test_Costas_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Costas")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_C_Low_Row(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/costa_low_row/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_C_Pull_Down_Aberto(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/costa_pull_down_aberto/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_C_Pull_Down_Supinado(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/costa_pull_down_supinado/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_C_Remada_Curva(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/costa_remada_curva/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Peito_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Peito")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_P_CO(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/peito_cross_over/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_P_Crucifixo(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/peito_crucifixo/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_P_peck_deck(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/peito_crucifixo/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_P_supino(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/peito_supino/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Quadriceps_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Quadriceps")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Q_cadeira_extensora(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/quadriceps_cadeira_extensora/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Q_cadeira_flexora(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/quadriceps_cadeira_flexora/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Q_hack_squat(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/quadriceps_hack_squat/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Q_Afundo(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/quadriceps_afundo/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Tríceps_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Tríceps")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_T_Frances(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/triceps_frances/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_T_Banco(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/triceps_banco/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_T_Cross_Corda(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/triceps_cross_corda/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_T_Cross_Unilateral(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/triceps_cross_unilateral/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Panturrilhas_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Panturrilhas")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_PT_Flexora_Vertical(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/panturrilha_flexora_vertical/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_PT_Flexora_Vertical(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/panturrilha_flexora_vertical/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_PT_Gemeos_Elevacao(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/panturrilha_gemeos_elevacao/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_PT_Gemeos_Maquina_em_pe(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/panturrilha_gemeos_maquina_em_pe/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_PT_Gemeos_Sentado(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/panturrilha_gemeos_sentado/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Gluteos_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Glúteos")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_G_Caneleira_Extensao(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/gluteo_caneleira_extensao/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_G_Caneleira(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/gluteo_caneleira/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_G_Crew(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/gluteo_crew/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_G_Maquina(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/gluteo_maquina/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Posterior_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Posterior")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Post_agachamento_smith(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/posterior_agachamento_smith/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Post_agachamento(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/posterior_agachamento/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Post_hack_squat(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/posterior_hack_squat/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Post_leg_curl(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/posterior_leg_curl/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_Antebraço_Choice(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/treino/")
        time.sleep(2)

        select = driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
        select.send_keys("Antebraço")
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_AB_Rosca_Inversa_Punho_Lateral(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/antebraco_rosca_inversa_punho_dumbell/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_AB_Rosca_Inversa_Punho(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/antebraco_rosca_inversa_punho/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_AB_Rosca_Punho_CO(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/antebraco_rosca_punho_cross_over/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_AB_Rosca_Punho(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/antebraco_rosca_punho/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_comentario = driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
        time.sleep(2)
        driver.quit()

    def test_medidas(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/medidas/")
        time.sleep(2)

        input_peito = driver.find_element(By.NAME, 'peito')
        input_peito.send_keys("10")
        time.sleep(2)

        input_costas = driver.find_element(By.NAME, 'costas')
        input_costas.send_keys("10")
        time.sleep(2)

        input_ombro = driver.find_element(By.NAME, 'ombro')
        input_ombro.send_keys("10")
        time.sleep(2)

        input_pescoco = driver.find_element(By.NAME, 'pescoco')
        input_pescoco.send_keys("10")
        time.sleep(2)

        input_braco = driver.find_element(By.NAME, 'braco')
        input_braco.send_keys("10")
        time.sleep(2)

        input_antebraco = driver.find_element(By.NAME, 'antebraco')
        input_antebraco.send_keys("10")
        time.sleep(2)

        input_quadril = driver.find_element(By.NAME, 'quadril')
        input_quadril.send_keys("10")
        time.sleep(2)

        input_cintura = driver.find_element(By.NAME, 'cintura')
        input_cintura.send_keys("10")
        time.sleep(2)

        input_coxa = driver.find_element(By.NAME, 'coxa')
        input_coxa.send_keys("10")
        time.sleep(2)

        input_panturrilha = driver.find_element(By.NAME, 'panturrilha')
        input_panturrilha.send_keys("10")
        time.sleep(2)

        input_salvar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        input_salvar.click()
        time.sleep(1)
        driver.quit()

    def test_Agua(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/consumo_agua/")
        time.sleep(2)

        input_data = driver.find_element(By.NAME, 'data')
        input_data.send_keys("19052023")
        time.sleep(2)

        input_hora = driver.find_element(By.NAME, 'hora')
        input_hora.send_keys("1030")
        time.sleep(2)

        select = driver.find_element(By.NAME, "quantidade")
        select.send_keys("250ml")
        time.sleep(2)

        enviar_agua = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar_agua.click()
        time.sleep(2)
        driver.quit()

    def test_cadastro(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/cadastro/")
        time.sleep(2)

        input_nome = driver.find_element(By.NAME, 'name')
        input_nome.send_keys('usuario')
        time.sleep(2)

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys('usuario@teste.com')
        time.sleep(2)

        input_senha = driver.find_element(By.NAME, 'senha')
        input_senha.send_keys('123456')
        time.sleep(2)

        input_peso = driver.find_element(By.NAME, 'peso')
        input_peso.send_keys('75')
        time.sleep(2)

        input_altura = driver.find_element(By.NAME, 'altura')
        input_altura.send_keys('175')
        time.sleep(2)

        input_idade = driver.find_element(By.NAME, 'idade')
        input_idade.send_keys('22')
        time.sleep(2)

        enviar = driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()

    # def test_login(self):
=======

    # def test_gyms(self):
>>>>>>> 016aa62d6123d26d0bebdd9cd83dd8ee610c98ab
    #     driver = webdriver.Chrome(options=chrome_options)
    #     input_email_login = driver.find_element(By.NAME, 'email')
    #     input_email_login.send_keys('usuario@teste.com')
    #     time.sleep(2)

    #     input_senha_login = driver.find_element(By.NAME, 'senha')
    #     input_senha_login.send_keys('123456')
    #     time.sleep(2)

    #     enviar_login = driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar_login.click()
    #     time.sleep(2)
    #     driver.quit()

    def test_perfil(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://127.0.0.1:8000/perfil/")
        time.sleep(2)
        driver.quit()