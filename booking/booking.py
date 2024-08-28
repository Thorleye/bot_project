import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_traceb): #needs 4 args or will throw error
        if self.teardown:
            self.quit()
    

    def landing_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = 'button[data-testid="header-currency-picker-trigger"]'
        self.find_element(By.CSS_SELECTOR, currency_element).click()
        selected_currency_element = 'div.c324bdcee4 ec7ca45eb7 ab9d1f83a2'
        self.find_element(By.CSS_SELECTOR, selected_currency_element).click()

    def select_location(self, location):
        search_field = self.find_element(By.XPATH, '//input[@id=":rh:"]')
        search_field.clear()
        search_field.send_keys(location)