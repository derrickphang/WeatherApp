"""
Author: Derrick Phang
Date: November 23, 2021
Description: Program contains a dboperations class with functions to
initialize and create a database, insert a dictionary of dictionaries, purge data, and fetch data.
"""

import datetime
import logging
from dbcm import DBCM


class DBOperations:
    """This class contains functions to create a database,
    insert a dictionary of dictionaries, and print the inserted rows."""

    logger = logging.getLogger("main." + __name__)

    def __init__(self) -> None:
        """Initializes global variables."""
        try:
            self.filename = './weather.sqlite'
            self.today = (datetime.datetime.today().strftime('%Y-%m-%d'))

        except Exception as e:
            self.logger.error(f"DBOperations: init: {e}")

    def initializedb(self) -> None:
        """Initializes and creates the table."""

        try:
            with DBCM(self.filename) as cur:
                cur.execute("""CREATE TABLE if not exists weatherdata
                                (
                                    id integer primary key autoincrement not null,
                                    sample_date text not null,
                                    location text not null,
                                    min_temp real not null,
                                    max_temp real not null,
                                    avg_temp real not null
                                );""")
        except Exception as e:
            self.logger.error(f"DBOperations: initializedb: {e}")

    def fetch_monthly_data(self, specified_year: str, specified_month: str) -> dict:
        """Returns monthly data sorted by the earliest
        date based on the specified month and year."""

        try:
            monthly_dict = {}

            sql = "'" + specified_year + "-" + specified_month + "-%%'"

            with DBCM(self.filename) as cur:
                for row in cur.execute("""SELECT sample_date, avg_temp FROM weatherdata
                 WHERE sample_date LIKE """ + sql + " ORDER BY sample_date"):

                    monthly_dict[row[0]] = row[1]

            return monthly_dict

        except Exception as e:
            self.logger.error(f"DBOperations: fetch_monthly_data: {e}")

    def fetch_data(self, start_year: str, end_year: str) -> dict:
        """Returns yearly data sorted by month based on the starting and ending year."""

        try:
            month_data = {}
            daily_temp = []
            i = 1

            sql = "'" + start_year + "-01-01' AND '" + end_year + "-12-31'"

            with DBCM(self.filename) as cur:

                for row in cur.execute("""SELECT sample_date, avg_temp, SUBSTR(sample_date, 6, 7)
                 AS month FROM weatherdata
                 WHERE sample_date BETWEEN""" + sql + "ORDER BY month ASC"):

                    database_month = int((row[0].split('-')[1]))
                    avg_temp = row[1]

                    if database_month == i:
                        daily_temp.append(avg_temp)
                    else:
                        month_data[i] = daily_temp
                        daily_temp = []
                        i = i + 1

                month_data[i] = daily_temp

            return month_data

        except Exception as e:
            self.logger.error(f"DBOperations: fetch_data: {e}")

    def row_checker(self) -> int:
        """Checks the quantity of rows in the database."""

        try:
            row_count = None

            with DBCM(self.filename) as cur:
                for row in cur.execute("SELECT COUNT(*) FROM weatherdata"):
                    row_count = row[0]

            return row_count

        except Exception as e:
            self.logger.error(f"DBOperations: row_checker: {e}")

    def last_date_checker(self) -> str:
        """Checks the last date in the database."""

        try:
            last_month = None
            last_year = None

            with DBCM(self.filename) as cur:
                for date in cur.execute("SELECT MAX(sample_date), avg_temp from weatherdata"):

                    tuple_date = date[0]
                    tuple_date = tuple_date.split('-')
                    tuple_year = tuple_date[0]
                    tuple_month = tuple_date[1]

                    if tuple_date != self.today:
                        last_month = tuple_month
                        last_year = tuple_year

            return last_month, last_year

        except Exception as e:
            self.logger.error(f"DBOperations: last_date_checker: {e}")

    def save_data(self, weather_dict: dict) -> None:
        """Receives a dictionary of dictionaries and inserts it into the database."""

        try:
            insert_sql = """INSERT INTO weatherdata (sample_date, location,
             min_temp, max_temp, avg_temp) values(?,?,?,?,?)"""

            for key, value in weather_dict.items():
                data = ()
                date = (key)
                location = ('Winnipeg, MB')
                for keys, values in value.items():
                    if keys == 'Max':
                        max = values
                    if keys == "Min":
                        min = values
                    if keys == "Mean":
                        avg = values
                data = (date, location, min, max, avg)

                with DBCM(self.filename) as cur:
                    cur.execute(insert_sql, data)

        except Exception as e:
            self.logger.error(f"DBOperations: save_data: {e}")

    def purge_all_data(self) -> None:
        """Deletes all data from the database."""

        try:
            with DBCM(self.filename) as cur:
                cur.execute("""DELETE FROM weatherdata""")

        except Exception as e:
            self.logger.error(f"DBOperations: purge_all_data: {e}")

    def purge_data(self, year: str, month: str) -> None:
        """Deletes data from a database based on specified year and month."""

        try:
            sql = "'" + year + "-" + month + "-%%" + "'"

            with DBCM(self.filename) as cur:
                cur.execute("""DELETE FROM weatherdata WHERE sample_date LIKE""" + sql)

        except Exception as e:
            self.logger.error(f"DBOperations: purge_data: {e}")
