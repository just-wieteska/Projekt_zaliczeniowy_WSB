import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Dane testowe
email = "justynatester2022@gmail.com"
haslo = "Castor123!"
komunikat = "Nie zaznaczono wymaganej zgody"

class CastoramaTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie do testow")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.castorama.pl")
        self.driver.implicitly_wait(10)

# #Zamkniecie przegladarki
    def tearDown(self):
        print("Zamkniecie przegladarki")
        self.driver.quit()

#Uruchomienie testow
    def testrejestracji(self):
        print("Uruchomienie testu nr 104")
        driver = self.driver
#Przejdz do strony rejestracji
        przejdz_do_rejestracji = driver.find_element(By.CSS_SELECTOR,"a.login-header__upper-link")
        przejdz_do_rejestracji.click()
#Wpisz poprawny email
        wpisz_email = driver.find_element(By.ID,"signInSignUp")
        wpisz_email.send_keys (email)
        sleep(2)
#Wpisz poprawne haslo
        wpisz_haslo = driver.find_element(By.ID,"signUpPassword")
        wpisz_haslo.send_keys (haslo)
        sleep(2)
#Cookie- by uzupelnic ulice nalezy zaaokceptowac cookie
        cookie = driver.find_element(By.CSS_SELECTOR, ".cookie-bar-close-button")
        cookie.click()
#Zalozenie konta
        zaloz_konto = driver.find_element(By.CSS_SELECTOR,"button.button-base:nth-child(6)")
        zaloz_konto.click()
# #Komunikat
        logowanie = driver.find_element(By.CSS_SELECTOR,"p.base-text").text
        assert logowanie == komunikat

if __name__ =='__main__':
    unittest.main()
