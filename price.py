from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

on = True
while on:
    def check_price():
        time.sleep(5)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.amazon.in/Apple-2024-MacBook-Laptop-chip/dp/B0CX23BZMY/ref=sr_1_2?crid=UAXG257R3EPG&dib=eyJ2IjoiMSJ9.0Ttf_tNbzm4xZ1oKs5QFYjtx6tyP5q2dYyCPX4_22ancfMyOYJoi6quVYyVY772ZoDmTS_ZjrjLBislIHI45-cOfzTEj9-oUNh7o8NkiDZvCyd7qUtc1ZEnO7sASKNTKDoxIXZ-lj37bovjYRHCf4-K_k-zcSI1McvWILAJiWhCjdan7MJnlM2cCvyo8FLIScq6QiSR7AFJqoQ_oNtd8QIOekZmme6GCjMJuNHUG9AE.tkOJHyTp6s8orzWwiL89qnhazUmdBvzM_Cavy5zYK9M&dib_tag=se&keywords=macbook%2Bair%2Bm3&qid=1719476930&sprefix=mac%2Caps%2C231&sr=8-2&th=1")
        try:
            price_element = driver.find_element(By.XPATH, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']//span[@aria-hidden='true']//span[@class='a-price-whole']")
            print(price_element.text)
        except Exception as e:
            print(e)
        finally:
            driver.close()
            driver.quit()
    check_price()
