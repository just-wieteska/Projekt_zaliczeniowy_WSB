import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Dane testowe
podstrona_rejestracji = "Rejestracja" \
                       ""
class CastoramaTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie do testow")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.castorama.pl")
        self.driver.implicitly_wait(10)
#Zamkniecie przegladarki
    def tearDown(self):
        print("Zamkniecie przegladarki")
        self.driver.quit()
#Uruchomienie testow
    def testNoNameInput(self):
        print("Uruchomienie testu nr 101")
        driver = self.driver
#Przejdz do strony logowania
        przejdz_do_logowania = driver.find_element(By.CSS_SELECTOR,"a.login-header__upper-link")
        przejdz_do_logowania.click ()
#Sprawdzenie poprawnosci strony
        test_podstrony = driver.find_element(By.CSS_SELECTOR,"div.section-base:nth-child(2) > h4:nth-child(1)").text
        assert test_podstrony == podstrona_rejestracji

if __name__ =='__main__':
    unittest.main()
