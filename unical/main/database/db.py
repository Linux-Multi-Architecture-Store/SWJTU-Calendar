import os
import sqlite3
import pathlib
from unical.main.utils.logger import Logger
import unical.main.database.utils as dbu


class Database:
    def __init__(self, db_path=None, logger: Logger=None):
        self.logger = logger
        if db_path is not None:
            self.db_path = db_path
            logger.info(f"Current db_path: \n {self.db_path}")
        else:
            self.db_path = pathlib.Path.home()
            self.db_path = os.path.join(self.db_path, ".config", "unical", "database")
            os.makedirs(self.db_path, exist_ok=True)
            self.db_path = os.path.join(self.db_path, "db.db")
            logger.war(f"db_path not given, using default path! \n {self.db_path}")

    def initialize_database(self):
        conn = sqlite3.connect(self.db_path)
        dbu.init_table(conn)

    def insert_database(self, sql_sentence: list):
        self.logger.info(f"Executing {sql_sentence}")
        conn = sqlite3.connect(self.db_path)
        dbu.execute_sqls(conn, sql_sentence)

    def query_database(self, sql_):
        self.logger.info(f"Executing {sql_}")
        conn = sqlite3.connect(self.db_path)
        return dbu.execute_query(conn, sql_)


