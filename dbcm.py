"""
Author: Derrick Phang
Date: November 23, 2021
Description: A Database Context Manager.
"""

import sqlite3
import logging

class DBCM:
    """Context manager that accesses an sqlite file."""

    logger = logging.getLogger("main." + __name__)

    def __init__(self, filename):
        """Initializes global variables."""
        try:
            self.connection = None
            self.cursor = None
            self.filename = filename

        except Exception as e:
            self.logger.error(f"DBCM: init: {e}")

    def __enter__(self):
        """Opens a connection and cursor."""
        try:
            self.connection = sqlite3.connect(self.filename)
            self.cursor = self.connection.cursor()
            return self.cursor

        except Exception as e:
            self.logger.error(f"DBCM: enter: {e}")

    def __exit__ (self, exc_type, exc_value, exc_trace):
        """Commits changes and closes cursor and connection."""
        try:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

        except Exception as e:
            self.logger.error(f"DBCM: exit: {e}")
