import os
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFullBA(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_home(self):
        self.driver.get(self.live_server_url)
        time.sleep(5)

    # def test_gyms(self):
    #     self.driver.get("http://127.0.0.1:8000/academias/")
    #     time.sleep(5)

        
    # def test_Biceps_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Bíceps")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_B_Rosca_Barra(self):
    #     self.driver.get("http://127.0.0.1:8000/biceps_rosca_com_barra/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)
        
    #     # input_voto = self.driver.find_element(By.ID, "star5")
    #     # input_voto.click()


    # def test_B_Rosca_Apoiada(self):
    #     self.driver.get("http://127.0.0.1:8000/biceps_rosca_apoiada/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)
    #     # input_voto = self.driver.find_element(By.ID, "star5")
    #     # input_voto.click()


    # def test_B_Rosca_Martelo(self):
    #     self.driver.get("http://127.0.0.1:8000/biceps_rosca_martelo/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)
    #     # input_voto = self.driver.find_element(By.ID, "star5")
    #     # input_voto.click()


    # def test_B_Rosca_Unilateral(self):
    #     self.driver.get("http://127.0.0.1:8000/biceps_rosca_unilateral/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     # input_voto = self.driver.find_element(By.ID, "star5")
    #     # input_voto.click()
    #     # time.sleep(2)

    # def test_Costas_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Costas")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)
    # def test_C_Low_Row(self):
    #     self.driver.get("http://127.0.0.1:8000/costa_low_row/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)
    # def test_C_Pull_Down_Aberto(self):
    #     self.driver.get("http://127.0.0.1:8000/costa_pull_down_aberto/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_C_Pull_Down_Supinado(self):
    #     self.driver.get("http://127.0.0.1:8000/costa_pull_down_supinado/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_C_Remada_Curva(self):
    #     self.driver.get("http://127.0.0.1:8000/costa_remada_curva/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Peito_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Peito")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_P_CO(self):
    #     self.driver.get("http://127.0.0.1:8000/peito_cross_over/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_P_Crucifixo(self):
    #     self.driver.get("http://127.0.0.1:8000/peito_crucifixo/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_P_peck_deck(self):
    #     self.driver.get("http://127.0.0.1:8000/peito_crucifixo/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_P_supino(self):
    #     self.driver.get("http://127.0.0.1:8000/peito_supino/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Quadriceps_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Quadriceps")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Q_cadeira_extensora(self):
    #     self.driver.get("http://127.0.0.1:8000/quadriceps_cadeira_extensora/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Q_cadeira_flexora(self):
    #     self.driver.get("http://127.0.0.1:8000/quadriceps_cadeira_flexora/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Q_hack_squat(self):
    #     self.driver.get("http://127.0.0.1:8000/quadriceps_hack_squat/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Q_Afundo(self):
    #     self.driver.get("http://127.0.0.1:8000/quadriceps_afundo/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Tríceps_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Tríceps")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_T_Frances(self):
    #     self.driver.get("http://127.0.0.1:8000/triceps_frances/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_T_Banco(self):
    #     self.driver.get("http://127.0.0.1:8000/triceps_banco/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_T_Cross_Corda(self):
    #     self.driver.get("http://127.0.0.1:8000/triceps_cross_corda/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_T_Cross_Unilateral(self):
    #     self.driver.get("http://127.0.0.1:8000/triceps_cross_unilateral/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Panturrilhas_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Panturrilhas")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_PT_Flexora_Vertical(self):
    #     self.driver.get("http://127.0.0.1:8000/panturrilha_flexora_vertical/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_PT_Flexora_Vertical(self):
    #     self.driver.get("http://127.0.0.1:8000/panturrilha_flexora_vertical/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_PT_Gemeos_Elevacao(self):
    #     self.driver.get("http://127.0.0.1:8000/panturrilha_gemeos_elevacao/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_PT_Gemeos_Maquina_em_pe(self):
    #     self.driver.get("http://127.0.0.1:8000/panturrilha_gemeos_maquina_em_pe/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)
    
    # def test_PT_Gemeos_Sentado(self):
    #     self.driver.get("http://127.0.0.1:8000/panturrilha_gemeos_sentado/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Gluteos_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Glúteos")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_G_Caneleira_Extensao(self):
    #     self.driver.get("http://127.0.0.1:8000/gluteo_caneleira_extensao/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_G_Caneleira(self):
    #     self.driver.get("http://127.0.0.1:8000/gluteo_caneleira/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_G_Crew(self):
    #     self.driver.get("http://127.0.0.1:8000/gluteo_crew/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_G_Maquina(self):
    #     self.driver.get("http://127.0.0.1:8000/gluteo_maquina/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Posterior_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Posterior")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Post_agachamento_smith(self):
    #     self.driver.get("http://127.0.0.1:8000/posterior_agachamento_smith/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Post_agachamento(self):
    #     self.driver.get("http://127.0.0.1:8000/posterior_agachamento/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Post_hack_squat(self):
    #     self.driver.get("http://127.0.0.1:8000/posterior_hack_squat/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Post_leg_curl(self):
    #     self.driver.get("http://127.0.0.1:8000/posterior_leg_curl/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_Antebraço_Choice(self):
    #     self.driver.get("http://127.0.0.1:8000/treino/")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.CSS_SELECTOR, "select[name='musculo']")
    #     select.send_keys("Antebraço")
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_AB_Rosca_Inversa_Punho_Lateral(self):
    #     self.driver.get("http://127.0.0.1:8000/antebraco_rosca_inversa_punho_dumbell/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_AB_Rosca_Inversa_Punho(self):
    #     self.driver.get("http://127.0.0.1:8000/antebraco_rosca_inversa_punho/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_AB_Rosca_Punho_CO(self):
    #     self.driver.get("http://127.0.0.1:8000/antebraco_rosca_punho_cross_over/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)

    # def test_AB_Rosca_Punho(self):
    #     self.driver.get("http://127.0.0.1:8000/antebraco_rosca_punho/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'autor')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_comentario = self.driver.find_element(By.NAME, 'texto')
    #     input_comentario.send_keys('abcd')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()
    #     time.sleep(2)
        
    # def test_medidas(self):
    #     self.driver.get("http://127.0.0.1:8000/medidas/")
    #     time.sleep(2)

    #     input_peito = self.driver.find_element(By.NAME, 'peito')
    #     input_peito.send_keys("10")
    #     time.sleep(2)

    #     input_costas = self.driver.find_element(By.NAME, 'costas')
    #     input_costas.send_keys("10")
    #     time.sleep(2)

    #     input_ombro = self.driver.find_element(By.NAME, 'ombro')
    #     input_ombro.send_keys("10")
    #     time.sleep(2)

    #     input_pescoco = self.driver.find_element(By.NAME, 'pescoco')
    #     input_pescoco.send_keys("10")
    #     time.sleep(2)

    #     input_braco = self.driver.find_element(By.NAME, 'braco')
    #     input_braco.send_keys("10")
    #     time.sleep(2)

    #     input_antebraco = self.driver.find_element(By.NAME, 'antebraco')
    #     input_antebraco.send_keys("10")
    #     time.sleep(2)

    #     input_quadril = self.driver.find_element(By.NAME, 'quadril')
    #     input_quadril.send_keys("10")
    #     time.sleep(2)

    #     input_cintura = self.driver.find_element(By.NAME, 'cintura')
    #     input_cintura.send_keys("10")
    #     time.sleep(2)

    #     input_coxa = self.driver.find_element(By.NAME, 'coxa')
    #     input_coxa.send_keys("10")
    #     time.sleep(2)

    #     input_panturrilha = self.driver.find_element(By.NAME, 'panturrilha')
    #     input_panturrilha.send_keys("10")
    #     time.sleep(2)

    #     input_salvar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     input_salvar.click()
    #     time.sleep(1)

    # def test_Agua(self):
    #     self.driver.get("http://127.0.0.1:8000/consumo_agua/")
    #     time.sleep(2)

    #     input_data = self.driver.find_element(By.NAME, 'Data')
    #     input_data.send_keys("19052023")
    #     time.sleep(2)

    #     input_hora = self.driver.find_element(By.NAME, 'Hora')
    #     input_hora.send_keys("1030")
    #     time.sleep(2)

    #     select = self.driver.find_element(By.NAME, "quantidade")
    #     select.send_keys("250ml")
    #     time.sleep(2)

    #     enviar_agua = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar_agua.click()
    #     time.sleep(2)

    # def test_cadastro(self):
    #     self.driver.get("http://127.0.0.1:8000/cadastro/")
    #     time.sleep(2)

    #     input_nome = self.driver.find_element(By.NAME, 'name')
    #     input_nome.send_keys('usuario')
    #     time.sleep(2)

    #     input_email = self.driver.find_element(By.NAME, 'email')
    #     input_email.send_keys('usuario@teste.com')
    #     time.sleep(2)

    #     input_senha = self.driver.find_element(By.NAME, 'password')
    #     input_senha.send_keys('123456')
    #     time.sleep(2)

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()

    #     input_email_login = self.driver.find_element(By.NAME, 'email')
    #     input_email_login.send_keys('usuario@teste.com')
    #     time.sleep(2)

    #     input_senha_login = self.driver.find_element(By.NAME, 'password')
    #     input_senha_login.send_keys('123456')
    #     time.sleep(2)

    #     enviar_login = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar_login.click()
    #     time.sleep(2)

    # def test_perfil(self):
    #     self.driver.get("http://127.0.0.1:8000/perfil/")
    #     time.sleep(2)