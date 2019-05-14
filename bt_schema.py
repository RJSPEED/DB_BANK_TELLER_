import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "bank_teller.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)


def schema(dbpath):
    with sqlite3.connect(DBPATH) as conn:
        cursor = conn.cursor()

        SQL = "DROP TABLE IF EXISTS accounts;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE accounts(
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_number VARCHAR(10),
                    pin VARCHAR(10),
                    balance FLOAT,
                    first_name VARCHAR(64),
                    last_name VARCHAR(64)
                    );"""
        cursor.execute(SQL)

if __name__ == "__main__":
    schema(DBPATH)
