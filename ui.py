"""
Author: Derrick Phang
Created: November 28, 2021
Description: A user interface that supplements the main module to plot weather data.
"""

import logging
import wx
from weather_frames import fraMain, fraAbout
from dboperations import DBOperations
from scrape_weather import WeatherScraper
from plot_operations import PlotOperations

class UI(fraMain):
    """Provides a user interface for the main module and plots weather data."""

    logger = logging.getLogger("main." + __name__)

    def __init__(self):
        try:
            super().__init__(None)
            self.db_operations = DBOperations()
            self.scrape_weather = WeatherScraper()
            self.plot_operations = PlotOperations()
            self.db_operations.initializedb()
            self.last_month_db = None
            self.last_year_db = None
        except Exception as e:
            self.logger.error(f"UI: init: {e}")

    def Btn_Plot_Daily_OnClick_Event( self, event ):
        """Handles the button click event for plot daily."""
        try:
            self.plot_operations.line_plot(self.db_operations.fetch_monthly_data(str(self.txt_Daily_Year_Input.Value), str(self.txt_Daily_Month_Input.Value)))
        except Exception as e:
            self.logger.error(f"UI: Btn_Plot_Daily_onClick_Event: {e}")

    def Btn_Plot_Monthly_OnClick_Event( self, event ):
        """Handles the button click event for plot monthly."""
        try:
            self.plot_operations.box_plot(self.db_operations.fetch_data(str(self.txt_Monthly_Start_Year_Input.Value), str(self.txt_Monthly_Start_End_Input.Value)), str(self.txt_Monthly_Start_Year_Input.Value), str(self.txt_Monthly_Start_End_Input.Value))
        except Exception as e:
            self.logger.error(f"UI: Btn_Plot_Monthly_OnClick_Event: {e}")

    def mnu_File_Download_Update_OnClick_Event( self, event ):
        """Handles the click event in menus to download update."""
        try:
            if self.db_operations.row_checker() > 0:
                self.last_month_db = str(self.db_operations.last_date_checker()[0])
                self.last_year_db = str(self.db_operations.last_date_checker()[1])

                self.db_operations.purge_data(self.last_year_db, self.last_month_db)
                self.db_operations.save_data(self.scrape_weather.scrape_url_new(self.last_year_db, self.last_month_db))
            else:
                self.db_operations.purge_all_data()
                self.db_operations.save_data(self.scrape_weather.scrape_url_all())
        except Exception as e:
            self.logger.error(f"UI: mnu_File_Download_Update_OnClick_Event: {e}")

    def mnu_File_Download_Full_OnClick_Event( self, event ):
        """Handles the click event in menus to download full data."""
        try:
            self.db_operations.purge_all_data()
            self.db_operations.save_data(self.scrape_weather.scrape_url_all())
        except Exception as e:
            self.logger.error(f"UI: mnu_File_Download_Full_OnClick_Event: {e}")

    def mnu_File_Exit_OnClick_Event( self, event ):
        """Handles the click event to exit the program."""
        try:
            self.Close()
        except Exception as e:
            self.logger.error(f"UI: mnu_File_Exit_OnClick_Event: {e}")

    def mnu_Help_About_OnClick_Event( self, event ):
        """Handles the click even to open the About menu."""
        app = wx.App()
        frm = AboutForm()
        frm.Show()
        app.MainLoop()

class AboutForm(fraAbout):
    def __init__(self):
        try:
            super().__init__(None)
        except Exception as e:
            self.logger.error(f"AboutForm: init")

    def btn_Close_OnClick_Event( self, event ):
        """Handles the click button even to close the form."""
        try:
            self.Close()
        except Exception as e:
            self.logger.error(f"AboutForm: btn_Close_OnClick_Event: {e}")
