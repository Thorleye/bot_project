import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self):
        super(Booking, self).__init__()

    def landing_page(self):
        self.get("https://www.booking.com")

    