import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Dane testowe
produkt = "Wiertarko-wkrętarka udarowa Makita DHP485 18 V"

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
    def testkoszyka(self):
        print("Uruchomienie testu nr 201")
        driver = self.driver
#Wyszukanie produktu
        wyszukaj_produkt = driver.find_element(By.ID,"search-input-desktop")
        wyszukaj_produkt.send_keys (produkt)

        kliknij_lupke = driver.find_element(By.CSS_SELECTOR,"#search_mini_formdesktop > button:nth-child(3)")
        kliknij_lupke.click ()

        znajdz_produkt = driver.find_element(By.CSS_SELECTOR,"#product-i-1150747 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)")
        znajdz_produkt.click ()
#Dodaj do koszyka
        dodaj_do_koszyka = driver.find_element(By.CSS_SELECTOR,"button.add-to-cart-button:nth-child(2)")
        dodaj_do_koszyka.click ()
#Przejdz do koszyka
        przejdz_do_koszyka = driver.find_element(By.CSS_SELECTOR,".button")
        przejdz_do_koszyka.click ()

#Test produktu w koszyku
        produkt_w_koszyku = driver.find_element(By.CSS_SELECTOR,".product-info__product-name-link").text
        assert produkt_w_koszyku == produkt

if __name__ =='__main__':
    unittest.main()
