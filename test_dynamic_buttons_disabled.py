"""
https://testpages.eviltester.com/styled/dynamic-buttons-simple.html

Kattintsunk rá az összes gombra.
Ellenőrizzük a sikeres visszajelzést assert-el (All Buttons Clicked)
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html'

class TestDynamicButtonsSimple:
    def setup_method(self):
        options = Options()
        options.add_argument("--disable-search-engine-choice-screen")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

    def test_click_all_buttons(self):
        btn00 = WebDriverWait(self.browser, 10, 0.2).until(EC.presence_of_element_located((By.ID, "button00")))
        btn00.click()

        btn01 = WebDriverWait(self.browser, 10, 0.2).until(EC.element_to_be_clickable((By.ID, "button01")))
        btn01.click()

        btn02 = WebDriverWait(self.browser, 10, 0.2).until(EC.element_to_be_clickable((By.ID, "button02")))
        btn02.click()

        btn03 = WebDriverWait(self.browser, 10, 0.2).until(EC.element_to_be_clickable((By.ID, "button03")))
        btn03.click()


        if (WebDriverWait(self.browser, 10, 0.2)
                .until_not(EC.text_to_be_present_in_element((By.ID, "buttonmessage"), "Click Buttons In Order"))):
            btn_msg = self.browser.find_element(By.ID, "buttonmessage")
            assert btn_msg.text == "All Buttons Clicked"
            # print(f"All buttons clicked: {btn_msg.text == 'All Buttons Clicked'}")

        btn_msg = self.browser.find_element(By.ID, "buttonmessage")
        assert btn_msg.text == "All Buttons Clicked"
        # print(f"All buttons clicked: {btn_msg.text == 'All Buttons Clicked'}")

