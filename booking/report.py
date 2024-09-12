from selenium.webdriver.remote.webelement import WebElement
#from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Report:
    def __init__(self, hotel_list:WebElement):
        self.hotel_list = hotel_list
        self.hotels = self.pull_hotels()

    def pull_hotels(self):
        return self.hotel_list.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_attributes(self):
        info = []
        for hotel in self.hotels:
            title = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML')
            price = hotel.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').get_attribute('innerHTML')
            #price= price[3]+' '+price[9:]
            rating = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]').get_attribute('innerHTML')
            rating=rating[66:69]
            info.append([title, price, rating])
        return info
        
    

