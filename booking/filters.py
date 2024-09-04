from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Filters:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def filter_star_rating(self, *star_rating):
        star_filter_box = self.driver.find_element(By.XPATH, '//div[@data-filters-group="class"]')

        for rating in star_rating:
            star_filter_rating = star_filter_box.find_element(By.XPATH, f'//div[@data-filters-item="class:class={rating}"]')
            click_star_filter = star_filter_rating.find_element(By.TAG_NAME, 'svg') #each clickbox is an svg in the parent div
            click_star_filter.click()
    
    def sort_lowest_price(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]').click()
        