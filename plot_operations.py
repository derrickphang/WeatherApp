"""
Author: Derrick Phang
Date: November 25, 2021
Description: This module receives and plots weather data.
"""

import logging
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker



class PlotOperations:
    """A program that creates a box plot or line plot based on weather data."""

    logger = logging.getLogger("main." + __name__)

    def __init__(self) -> None:
        pass

    def box_plot(self, weather_data: dict, start_year: str, end_year: str):
        """Creates a box plot based on weather temperatures
        from a dictionary and user input of starting and ending year."""

        try:
            date_string = start_year + ' to ' + end_year
            fig = plt.figure('Monthly Temperature Distribution for: ' + date_string)
            ax = fig.add_subplot()
            ax.set_title('Monthly Temperature Distribution for: ' + date_string)
            ax.set_xlabel('Month')
            ax.set_ylabel('Temperature (Celsius)')
            ax.boxplot(weather_data.values())
            labels = ax.get_xticks().tolist()
            ax.xaxis.set_major_locator(mticker.FixedLocator(labels))
            ax.set_xticklabels(weather_data.keys())

            plt.show()

        except Exception as e:
            self.logger.error(f"PlotOperations: box_plot: {e}")

    def line_plot(self, weather_data: dict):
        """Creates a line plot based on a weather temperatures from a dictionary."""

        try:

            weather_date = []
            weather_temp = []

            for key, value in weather_data.items():
                try:
                    weather_date.append(key)
                    weather_temp.append(value)

                except Exception as e:
                    self.logger.error(f"line_plot: loop: {e}")

            xlabels = list(range(len(weather_date)))

            plt.figure('Daily Avg Temperatures')
            plt.title('Daily Avg Temperatures')
            plt.plot(weather_temp)
            plt.ylabel('Avg Daily Temp')
            plt.xlabel('Day of Month')
            plt.xticks(xlabels, weather_date)
            plt.xticks(rotation=45)
            plt.show()

        except Exception as e:
            self.logger.error(f"PlotOperations: line_plot: {e}")
