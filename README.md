# WeatherApp
Winnipeg Weather Processor
Overall - Scrapes weather data from the Environment Canada website, inserts the data into a database, plots the weather by month or by year based on user input.

App created in Python

Contains:
dbcm.py - Database Context Manager
dboperations.py - Database class to initialize and create a database, insert a dictionary of dictionaries, purge data, and fetch data.
plot_operations.py - Plots weather data
scrape_weather.py - Web scraper that scrapes data from the Environmental Canada Website
ui.py - Initilizes the UI for the program
weather_frames.py - Frames created by wxFormBuilder
weather_processor.py - Opens the UI to process and plot weather data
