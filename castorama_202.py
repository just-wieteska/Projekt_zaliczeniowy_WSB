import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Dane testowe
produkt = "Wiertarko-wkrętarka udarowa Makita DHP485 18 V"
mail = "justynatester2022@gmail.com"
last_name = "Bravo"
first_name = "John"
country = "Polska"
zipcode = "54-104"
street = "Maslicka"
number = "12345"
phone = "123456789"
expected_message = "Błąd danych do wysyłki"

class CastoramaTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie do testow")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.castorama.pl")
        self.driver.implicitly_wait(10)
#Zamkniecie przegladarki
    def tearDown (self):
        print("Zamkniecie przegladarki")
        self.driver.quit()

#Uruchomienie testow
    def testkoszyka(self):
        print("Uruchomienie testu nr 202")
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
#Wybierz sklep
        wybor_sklepu = driver.find_element(By.CSS_SELECTOR,".page-checkout-cart__choose-store-monit > button:nth-child(2)")
        wybor_sklepu.click ()
        wybor_magnolia = driver.find_element(By.CSS_SELECTOR,"div.popup-choose-availability-market-item:nth-child(85) > button:nth-child(2)")
        wybor_magnolia.click ()
        sleep(3)

#Przejdz do zamownienia
        zamownienie = driver.find_element(By.CSS_SELECTOR,".checkout-cart-summary-old__go-to-order-button")
        zamownienie.click ()

        sleep(3)
#Odklikaj pojawiajace sie okienko - reklama
        castomat = driver.find_element(By.ID, "dws-shop-popup-mask")
        castomat.click()
#Kupuj jako gosc
        gosc = driver.find_element(By.CSS_SELECTOR,".login-page__link")
        gosc.click()

#Uzupenij dane zamawiajacego
        sleep (4)
        wprowadz_mail = driver.find_element(By.ID, "email")
        wprowadz_mail.send_keys(mail[0:1])
        wprowadz_mail.send_keys(mail[1:len(mail)])

        nazwisko = driver.find_element(By.ID, "lastname")
        nazwisko.send_keys(last_name[0:1])
        nazwisko.send_keys(last_name[1:len(last_name)])

        kod_pocztowy = driver.find_element(By.ID, "zipCode")
        kod_pocztowy.send_keys(zipcode)

#Cookie- by uzupelnic ulice nalezy zaaokceptowac cookie
        cookie = driver.find_element(By.CSS_SELECTOR,".cookie-bar-close-button")
        cookie.click()

        ulica = driver.find_element(By.ID, "vs4__combobox")
        ulica.click()
        wybierz_ulice = driver.find_element(By.ID, "vs4__option-1")
        wybierz_ulice.click()
        numer_domu = driver.find_element(By.ID, "buildingNumber")
        numer_domu.send_keys(number[0:1])
        numer_domu.send_keys(number[1:len(number)])

        telefon = driver.find_element(By. ID, "areaCodeWithPhone")
        telefon.send_keys(phone)

#Wybierz opcje dostawy - odbior osobisty
        odbior = driver.find_element(By.CSS_SELECTOR,"div.multistep-checkout-shipping-methods-form__shipping-option-wrapper:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)")
        odbior.click()

#Wybierz sposob platnosci
        platnosc = driver.find_element(By.CSS_SELECTOR,"button.button-base--blue:nth-child(1)")
        platnosc.click()

#Test komunikatu
        sleep(2)
        komunikat = driver.find_element(By.CSS_SELECTOR,"p.base-text:nth-child(1)").text
        assert komunikat == expected_message

if __name__ =='__main__':
    unittest.main()

