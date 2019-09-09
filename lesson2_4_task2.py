from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/explicit_wait2.html"

def f(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    message = browser.find_element_by_id("price")
    assert "100" in message.text
#    print(price)
    book_button = browser.find_element_by_css_selector("#book")
    book_button.click()


    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    print(x)
    a = f(x)
    print(a)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(a)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла