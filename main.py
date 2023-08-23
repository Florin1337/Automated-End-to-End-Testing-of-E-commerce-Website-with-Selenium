from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.automationexercise.com/")

lista_produse = ["Sleeveless Dress", "Men Tshirt", "Soft Stretch Jeans"]

login = driver.find_element("xpath", "//*[@id=\"header\"]/div/div/div/div[2]/div/ul/li[4]/a")
login.click()
login = driver.find_element("name", "email")
login.send_keys("bocseflorin@yahoo.com")
login = driver.find_element("name", "password")
login.send_keys("bocseflorin")
login = driver.find_element("xpath", "//*[@id=\"form\"]/div/div/div[1]/div/form/button")
login.click()

for a in range(0, len(lista_produse)):
    driver.get("https://www.automationexercise.com/products")
    search_products = driver.find_element("id", "search_product")
    search_products.click()
    search_products.send_keys(f"{lista_produse[a]}")
    search_products = driver.find_element("id", "submit_search")
    search_products.click()

    add_cart = driver.find_element("xpath", "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a")
    add_cart.click()
    add_cart = driver.find_element("xpath", "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
    add_cart.click()
    driver.get("https://www.automationexercise.com/view_cart")

time.sleep(3)
checkout = driver.find_element("css selector", "#do_action > div.container > div > div > a")
checkout.click()
checkout = driver.find_element("xpath", "//*[contains(text(), 'Place Order')]")
driver.execute_script("arguments[0].scrollIntoView();", checkout)
checkout.click()
checkout = driver.find_element("name", "name_on_card")
checkout.send_keys("florin bocse")
checkout = driver.find_element("name", "card_number")
checkout.send_keys("0987654321")
checkout = driver.find_element("name", "cvc")
checkout.send_keys("112")
checkout = driver.find_element("name", "expiry_month")
checkout.send_keys("05")
checkout = driver.find_element("name", "expiry_year")
checkout.send_keys("2025")
checkout = driver.find_element("id", "submit")
checkout.click()
driver.get("https://www.automationexercise.com/")

