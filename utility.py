import pyodbc
from colorama import Fore


class Datas:

    def __init__(self):
        self.join = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                                   "Server};SERVER=LAPTOP-JUC4Q6HC;"
                                   "DATABASE=TRIVIA;"
                                   "Trusted_connection=yes")
        self.cursor = self.join.cursor()


