import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        currency_element = '//*[@id="b2indexPage"]/div[2]/div/div/header/div/nav[1]/div[2]/span[1]/button/span'
        self.find_element(By.XPATH, currency_element).click()
        selected_currency_element = '//*[@id="b2indexPage"]/div[42]/div/div/div/div/div[2]/div/div[3]/div/div/div/ul[13]/li[2]/button/div/div'
        self.find_element(By.XPATH, selected_currency_element).click()

    def select_location(self, location):
        search_field = self.find_element(By.XPATH, '//input[@id=":rh:"]')
        search_field.clear()
        search_field.send_keys(location)
        search_field.send_keys(Keys.ESCAPE)
        self.find_element(By.ID, "autocomplete-result-0").click()
    
    def select_dates(self, check_in, check_out): #YYYY-MM-DD
        self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in}"]').click()
        self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out}"]').click()

    def select_adults(self, adult_target_count):
        self.find_element(By.CLASS_NAME, "a6391e882c").click()
        minus_one_adult = self.find_element(By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[1]') #adult -1
        plus_one_adult = self.find_element(By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[2]')

        if adult_target_count == 1:
            minus_one_adult.click()
        #2 is default - pass on 2
        elif adult_target_count > 2:
            for _ in range(adult_target_count -2 ):
                plus_one_adult.click()
           
        self.find_element(By.XPATH, '//*[@id=":ri:"]/button').click() #done button

    
    def click_search_button(self):
        self.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[4]/button/span').click()
