import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "bank_teller.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def seed(dbpath):
    accounts = [
            ("123456", "9195", 850.00, "Richard", "Speed"),         
            ("123457", "9111", 2850.00, "Jayne", "Speed"),         
            ("123458", "9190", 5850.00, "Frazer", "Speed"),
            ("123459", "9199", 9850.00, "Ethan", "Speed")]

    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor()
        SQL = """INSERT INTO accounts(account_number, pin, balance, first_name, last_name) VALUES (?, ?, ?, ?, ?);"""
        for account in accounts:
            curs.execute(SQL, account)

if __name__ == "__main__":
    seed(DBPATH)
