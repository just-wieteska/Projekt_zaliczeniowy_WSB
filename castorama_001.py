import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Dane testowe
strona_glowna = "Zakupy w Castorama"

class CastoramaTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie do testow")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.castorama.pl")
        self.driver.implicitly_wait(10)

# Zamkniecie przegladarki
    def tearDown(self):
        print("Zamkniecie przegladarki")
        self.driver.quit()
#Uruchomienie testow
    def testNoNameInput(self):
        print("Uruchomienie testu nr 001")
        driver = self.driver
#Znajdz cookies na stronie startowej i je zakceptuj
        cookies = driver.find_element(By.CSS_SELECTOR,".cookie-bar-close-button")
        cookies.click ()
#Sprawdz czy jestes na poprawnej stronie
        test_strony = driver.find_element(By.CSS_SELECTOR,".shopping-pictograms__title").text
        assert test_strony == strona_glowna

if __name__ =='__main__':
    unittest.main()
