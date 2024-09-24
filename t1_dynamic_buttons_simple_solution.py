"""
https://testpages.eviltester.com/styled/dynamic-buttons-simple.html

Kattintsunk rá az összes gombra.
Ellenőrizzük a sikeres visszajelzést assert-el (All Buttons Clicked)
"""

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://testpages.eviltester.com/styled/dynamic-buttons-simple.html'
options = Options()
options.add_argument('window-position=2000,50')
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get(URL)
browser.maximize_window()

message = browser.find_element(By.ID, "buttonmessage")

start_button = browser.find_element(By.ID, "button00")
start_button.click()

button_1 = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "button01")))
button_1.click()
button_2 = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "button02")))
button_2.click()
button_3 = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "button03")))
button_3.click()

assert message.text == "All Buttons Clicked"


