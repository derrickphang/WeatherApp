"""
Author: Derrick Phang
Created: November 21, 2021
Description: Scrapes weather data from the Environment Canada website.
"""

from html.parser import HTMLParser
import urllib.request
import datetime
import logging

class WeatherScraper(HTMLParser):
    """This class parses HTML from the Environment Canada website."""

    logger = logging.getLogger("main." + __name__)

    def __init__(self):
        try:
            HTMLParser.__init__(self)
            self.daily_temps = {}
            self.daily_weather = {}
            self.tbody_tag = 0
            self.h1_tag = 0
            self.th_tag = 0
            self.tr_tag = 0
            self.td_max_temp_tag = 0
            self.td_min_temp_tag = 0
            self.td_mean_temp_tag = 0
            self.month = None
            self.year = None
            self.date = None
            self.todays_date = (datetime.datetime.today().strftime('%Y-%m'))
            self.todays_year = (self.todays_date.split("-")[0])
            self.todays_month = (self.todays_date.split("-")[1])
            self.new_year = None
            self.new_month = None
            self.url = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2021&Day=1&Year='
            self.todays_url = self.url + self.todays_year + '&Month=' + self.todays_month
            self.new_url = None
            self.weather = {}

        except Exception as e:
            self.logger.error(f"WeatherScraper: init: {e}")

    def handle_starttag(self, tag: str, attrs) -> None:
        """Finds the start tag of 'body', 'th', 'tr', 'h1', and 'td in HTML."""
        try:
            # Value of 0 is OFF, Value of 1 is ON, Value of 2 is an additional flag check
            if tag == 'tbody':
                self.tbody_tag = 1
            if tag == 'th':
                self.th_tag = 1
            if tag == 'tr':
                self.tr_tag = 1
            if tag == 'h1':
                self.h1_tag = 1
            if tag == 'td' and self.tbody_tag == 1 and self.tr_tag == 1 and self.td_max_temp_tag != 2:
                self.td_max_temp_tag = 1
            if tag == 'td' and self.td_max_temp_tag == 2 and self.td_min_temp_tag != 2:
                self.td_min_temp_tag = 1
            if tag == 'td' and self.td_min_temp_tag == 2 and self.td_mean_temp_tag != 2:
                self.td_mean_temp_tag = 1

        except Exception as e:
            self.logger.error(f"WeatherScraper: handle_starttag: {e}")

    def handle_endtag(self, tag: str) -> None:
        """Finds the end tag of 'body', 'th', 'tr', 'h1', and 'td in HTML.'"""
        try:
            # Value of 0 is OFF, Value of 1 is ON, Value of 2 is an additional flag check
            if tag == 'tbody':
                self.tbody_tag = 2
            if tag == 'td':
                self.td_max_temp_tag = 2
                if self.td_min_temp_tag == 1:
                    self.td_min_temp_tag = 2
                if self.td_mean_temp_tag == 1:
                    self.td_mean_temp_tag = 2
            if tag == 'tr':
                self.tr_tag = 0
                self.td_max_temp_tag = 0
                self.td_min_temp_tag = 0
                self.td_mean_temp_tag = 0
            if tag == 'h1':
                self.h1_tag = 2
            if tag == 'th':
                if self.th_tag == 1:
                    self.th_tag = 2

        except Exception as e:
            self.logger.error(f"WeatherScraper: handle_endtag: {e}")

    def handle_data(self, data: str) -> None:
        """Finds the data within the 'body' tag and 'a' tag in HTML."""
        try:
            self.new_month = self.todays_month
            self.new_year = self.todays_year

            # if table head is ON and table body tag is ON, proceed
            if self.th_tag == 1 and self.tbody_tag == 1:

                # if the length of the data is equal to 2 digits (to find temperature), proceed
                if len(data) == 2:
                    self.date = datetime.datetime.strptime(self.year + "-" + str(self.month) + "-" + data, "%Y-%m-%d").date()
                    self.daily_temps = {}

                # if the length of the data is greater or equal to 3, turn off the table head tag
                if len(data) >= 3:
                    self.th_tag = 0

            # if the heading tag is ON, split the heading to determine the month and year of the URL
            if self.h1_tag == 1:
                date = (data.split("for ")[1])
                self.month = (date.split(" ")[0])
                self.year = (date.split(" ")[1])
                parse_month = datetime.datetime.strptime(self.month, "%B")
                self.month = parse_month.month

            # if the table body and table data tag (for max temp) is ON and
            # table head is CHECKED, save data into 'Max'
            if self.tbody_tag == 1 and self.td_max_temp_tag == 1 and self.tr_tag == 1 and self.th_tag == 2:
                if data != '' and 'E' not in data and 'M' not in data:
                    self.daily_temps['Max'] = data

            # if the table body and table data tag (for max temp) is ON and
            # table head is CHECKED, save data into 'Min'
            if self.td_min_temp_tag == 1 and self.tbody_tag == 1 and self.tr_tag == 1 and self.th_tag == 2:
                if data != '' and 'E' not in data and 'M' not in data:
                    self.daily_temps['Min'] = data

            # if the table body and table data tag (for max temp) is ON and
            # table head is CHECKED, save data into 'Mean'
            if self.td_mean_temp_tag == 1 and self.tbody_tag == 1 and self.tr_tag == 1 and self.th_tag == 2:
                if data != '' and 'E' not in data and'M' not in data:
                    self.daily_temps['Mean'] = data
                    self.daily_weather[self.date] = self.daily_temps

        except Exception as e:
            self.logger.error(f"WeatherScraper: handle_data: {e}")

    def scrape_url_new(self, year: str, month: str):
        """Scrapes URL based on the specified year and month.
            Returns a dictionary with weather data."""

        try:
            self.new_month = month
            self.new_year = year
            new_url = self.url + self.new_year + '&Month=' + self.new_month

            # Opens the URL based
            with urllib.request.urlopen(new_url) as response:

                html = str(response.read())
                check_website = WeatherScraper()
                check_website.feed(html)
                count = 1

                # If the specified month is equal to the heading month AND
                # specifed year is equal to the heading year, proceed
                while int(self.new_month) == int(check_website.month) and int(self.new_year) == int(check_website.year):
                    self.new_url = self.url + self.new_year + '&Month=' + self.new_month

                    # Open the URL with new month and year.
                    with urllib.request.urlopen(self.new_url) as response:

                        html = str(response.read())

                    myparser = WeatherScraper()
                    myparser.feed(html)

                    # While the updated month is equal to the
                    # headline month of the webpage, proceed
                    while int(self.new_month) == int(myparser.month):

                        # While the count is less than or equal to the length of temperatures in the
                        # month, create weather dictionary based on key value pairs
                        while count <= len(myparser.daily_weather):
                            print('Retrieving ' + self.new_year + '-' + self.new_month)

                            for key, value in myparser.daily_weather.items():
                                self.weather[key] = value
                                count = count + 1

                            else:
                                count = 1
                                break

                        self.new_month = str(int(self.new_month) + 1)

                        # if the counter goes up to 13, set it back to 1 and update the url
                        if int(self.new_month) == 13 and int(self.new_year) <= int(self.todays_year):
                            self.new_month = str('1')
                            check_website.month = str('1')
                            self.new_year = str(int(self.new_year) + 1)
                            check_website.year = str(int(myparser.year) + 1)

                        self.new_url = self.url + self.new_year + '&Month=' + self.new_month

                        # check new url and check the headline month
                        with urllib.request.urlopen(self.new_url) as response:
                            html = str(response.read())
                            myparser = WeatherScraper()
                            myparser.feed(html)

                    return self.weather

        except Exception as e:
            self.logger.error(f"WeatherScraper: scrape_url_new: {e}")

    def scrape_url_all(self):
        """Scrapes URL for all data. Returns a dictionary with weather data."""
        try:
            self.new_month = self.todays_month
            self.new_year = self.todays_year

            # Open URL with today's date
            with urllib.request.urlopen(self.todays_url) as response:

                html = str(response.read())
                check_website = WeatherScraper()
                check_website.feed(html)
                count = 1

                # If the specified month is equal to the heading month
                # AND specifed year is equal to the heading year, proceed
                while int(self.new_month) == int(check_website.month) and int(self.new_year) == int(check_website.year):

                    self.new_url = self.url + self.new_year + '&Month=' + self.new_month

                    # Open the URL with new month and year
                    with urllib.request.urlopen(self.new_url) as response:
                        html = str(response.read())

                    myparser = WeatherScraper()
                    myparser.feed(html)

                    # While the updated month is equal the the
                    # headline month of the webpage, proceed
                    while int(self.new_month) == int(myparser.month):

                        # While the count is less than or equal to the length of temperatures
                        # in the month, create weather dictionary based on key value pairs
                        while count <= len(myparser.daily_weather):
                            print('Retrieving ' + self.new_year + '-' + self.new_month)

                            for key,value in myparser.daily_weather.items():
                                self.weather[key] = value
                                count = count + 1

                            else:
                                count = 1
                                break

                        self.new_month = str(int(self.new_month) - 1)

                        # if the counter goes down to 0, set it back to 12 and update the url
                        if int(self.new_month) == 0:
                            self.new_month = str('12')
                            check_website.month = str('12')
                            self.new_year = str(int(self.new_year) - 1)
                            check_website.year = str(int(myparser.year) - 1)

                        self.new_url = self.url + self.new_year + '&Month=' + self.new_month

                        # check new url and check the headline month
                        with urllib.request.urlopen(self.new_url) as response:

                            html = str(response.read())
                            myparser = WeatherScraper()
                            myparser.feed(html)

                    return self.weather

        except Exception as e:
            self.logger.error(f"WeatherScraper: scrape_url_all: {e}")
