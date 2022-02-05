"""
Author: Derrick Phang
Created: November 21, 2021
Description: Opens the UI to process and plot weather data.
"""

import logging
import logging.handlers
import wx
from ui import UI

class WeatherProcessor:
    """Opens the UI to process and plot weather data."""

    logger = logging.getLogger("main." + __name__)

    def __init__(self) -> None:
        pass

    def main(self):
        """Main function to process and plot weather data."""

        try:
            app = wx.App()

            frm = UI()
            frm.Show()

            app.MainLoop()
        except Exception as e:
            self.logger.error(f"WeatherProcessor: main: {e}")

if __name__ == "__main__":
    
    try:
        logger = logging.getLogger("main")
        logger.setLevel(logging.DEBUG)
        fh = logging.handlers.RotatingFileHandler(filename="threads.log",
                                                    maxBytes=10485760,
                                                    backupCount=10)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Main Thread Started")

        WeatherProcessor().main()
    except Exception as e:
        logger.error(f"main_thread:main: {e}")
