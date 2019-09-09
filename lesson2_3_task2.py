from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/alert_accept.html"

def f(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

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