from booking.booking import Booking

with Booking(teardown=True) as bot:
    bot.landing_page()
   # bot.change_currency()
    bot.select_location("New York City")