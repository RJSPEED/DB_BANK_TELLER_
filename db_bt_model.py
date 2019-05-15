import os
import sqlite3

DIR = os.path.dirname(__file__)
DATAFILENAME = "bank_teller.db"  # use your teller filename
DATAPATH = os.path.join(DIR, DATAFILENAME)

class Account:

    def __init__(self, account_num="", pin="", balance="", f_name="", l_name=""):
        # populate self.attributes for a bank account
        self.account_num = account_num
        self.pin = pin
        self.balance = balance
        self.f_name = f_name
        self.l_name = l_name 

    def create_account(self):        
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            SQL = """SELECT max(account_number) FROM accounts;"""
            cursor.execute(SQL)
            result = cursor.fetchone()
            max_account = int(result[0]) + 1
            
            SQL = """INSERT INTO accounts (account_number, first_name, 
                     last_name, pin, balance) 
                     VALUES (?, ?, ?, ?, ?);"""
            values = (max_account, self.f_name, self.l_name, self.pin, 0.00)
            cursor.execute(SQL, values)
        
            return max_account

    def validate(self):
        # return True or False if the account_num and pin is in the datafile
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            SQL = """SELECT * FROM accounts 
                     WHERE account_number = ? and pin = ?;"""
            cursor.execute(SQL, (self.account_num,self.pin))
            result = cursor.fetchone()
            if not result:
                return False
            else:
                return True    

    def load_account_data(self):
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            SQL = """SELECT first_name, last_name FROM accounts 
                     WHERE account_number = ?;"""
            cursor.execute(SQL, (self.account_num,))
            result = cursor.fetchone()
            
            return result[0] + " " + result[1] + " (" + self.account_num + ")"

    def get_bal(self):
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            SQL = """SELECT balance FROM accounts 
                     WHERE account_number = ?;"""
            cursor.execute(SQL, (self.account_num,))
            result = cursor.fetchone()
            
            return result[0]        

    def deposit(self, amount):
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            SQL = """UPDATE accounts SET balance = balance + ? 
                     WHERE account_number = ?;"""
            cursor.execute(SQL, (amount,self.account_num))
            
            SQL = """SELECT balance FROM accounts 
                     WHERE account_number = ?;"""
            cursor.execute(SQL, (self.account_num,))
            result = cursor.fetchone()
            
            return result[0]        
   
    def withdraw(self, amount):
        # decrease the balance of this account
        # raise ValueError if there is insufficient funds
        amount = float(amount)
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            SQL = """SELECT balance FROM accounts 
                     WHERE account_number = ?;"""
            cursor.execute(SQL, (self.account_num,))
            result = cursor.fetchone()
            
            if amount > result[0]:
                return False
            else:
                SQL = """UPDATE accounts SET balance = balance - ? 
                         WHERE account_number = ?;"""
                cursor.execute(SQL, (amount,self.account_num))
                
                return result[0] - amount
            