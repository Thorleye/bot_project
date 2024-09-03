from booking.booking import Booking

with Booking(teardown=True) as bot:
    bot.landing_page()
    bot.change_currency("USD")
    bot.select_location("New York City")
    bot.select_dates(check_in="2024-09-25", check_out="2024-09-30")
    bot.select_adults(1)
    bot.click_search_button()
    bot.apply_filters()