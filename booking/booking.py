import booking.constants as const
from booking.filters import Filters
from booking.report import Report

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

    def click_currency(self):
        currency_button = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_button.click()

    def change_currency(self, currency):
        try:            
            self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]').click()
            self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]').click()
        except:
            pass
        selected_currency_element =  f'//div[text()="{currency}"]'
        self.find_element(By.XPATH, selected_currency_element).click()  

    def select_location(self, location):
        search_field = self.find_element(By.XPATH, '//input[@id=":rh:"]')
        search_field.clear()
        search_field.send_keys(location)
        search_field.send_keys(Keys.ESCAPE)
        #self.find_element(By.ID, "autocomplete-result-0").click()  ----too slow
        self.find_element(By.XPATH, f"//div[contains(text(), '{location}')]").click()
    
    def select_dates(self, check_in, check_out): #YYYY-MM-DD
        self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in}"]').click()
        self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out}"]').click()

    def select_adults(self, adult_target_count):
        self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]').click()
        minus_one_adult = self.find_element(By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[1]') #adult -1
        plus_one_adult = self.find_element(By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[2]') #adult +1

        if adult_target_count == 1:
            minus_one_adult.click()
        #2 is default - pass on 2
        elif adult_target_count > 2:
            for _ in range(adult_target_count -2 ):
                plus_one_adult.click()
           
        self.find_element(By.XPATH, '//*[@id=":ri:"]/button').click() #done button

    
    def click_search_button(self):
        self.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def search(self):
        self.find_element(By.XPATH, '//input[@id=":rh:"]').send_keys(Keys.ENTER)

    
    def apply_filters(self):
        filters = Filters(driver=self)
        filters.filter_star_rating(3,4,5)
        filters.sort_lowest_price()

    def scroll_to_bottom(self):
        self.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    def scroll_to_top(self):
        self.execute_script("window.scrollTo(0, 0);")

        
    def report_results(self):
        report = Report(self)
        print(report.pull_attributes())
        #print(results.pull_ratings())
        #print(results.pull_prices())

        #l = report.results
        #for i in l:
        #    print(i.__getattribute__("innerHTML"))
        
        #hotel_info = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="title"]')
        #for title in hotel_info:
        #    print(title.get_attribute("innerHTML"))
        #report = Report(hotel_list)
        #report.pull_title()