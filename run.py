from booking.booking import Booking

with Booking(teardown=True) as bot:
    try:
        bot.landing_page()
        bot.close_popup()
        bot.click_currency()
        bot.change_currency("USD")
        bot.select_location("New York City")
        bot.select_dates(check_in="2024-09-25", check_out="2024-09-30")
        bot.select_adults(1)
        bot.click_search_button()
        #temp = input("wait")
        bot.scroll_to_bottom()
        bot.apply_filters()
        bot.report_results()
        
    
    except:
        raise